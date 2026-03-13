from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from datetime import timedelta
# from django.urls import reverse


def get_the_next_day():
    return timezone.now() + timedelta(hours=24)


class User(AbstractUser):
    about = models.TextField(blank=True, max_length=150, verbose_name="О пользователе")
    avatar = models.ImageField(blank=True, upload_to="avatars/", verbose_name="Аватар пользователя")
    is_admin = models.BooleanField(default=False, verbose_name="Админ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return self.username


class Item(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="items", verbose_name="Создатель")
    name = models.CharField(max_length=50, verbose_name="Название")
    about = models.TextField(blank=True, verbose_name="О предмете")
    characteristics = models.TextField(blank=True, verbose_name="Характеристики")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
    
    def __str__(self):
        return self.name


class Location(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="locations", verbose_name="Создатель")
    name = models.CharField(max_length=50, verbose_name="Название")
    about = models.TextField(blank=True, verbose_name="О локации")
    rules = models.TextField(blank=True, verbose_name="Дополнительные правила")
    items = models.ManyToManyField(Item, related_name="locations", verbose_name="Предметы на локации")
    picture = models.ImageField(blank=True, upload_to="locations/", verbose_name="Изображение локации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
    
    def __str__(self):
        return self.name


class Character(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="characters", verbose_name="Владелец персонажа")
    name = models.CharField(max_length=50, verbose_name="Имя")
    about = models.TextField(blank=True, verbose_name="О персонаже")
    picture = models.ImageField(blank=True, upload_to="characters/", verbose_name="Изображение персонажа")
    items = models.ManyToManyField(Item, through="CharactersItem", related_name="characters", verbose_name="Предметы персонажа")
    status = models.CharField(max_length=50, verbose_name="Статус")
    characteristics = models.TextField(blank=True, verbose_name="Характеристики")
    at_location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE, related_name="characters", verbose_name="Персонаж в локации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"
    
    def __str__(self):
        return self.name


class Game(models.Model):
    STATUS_CHOICES = [
        ("active", "Активна"),
        ("paused", "Приостановлена"),
        ("ended", "Завершена"),
        ("abandoned", "Брошена"),
        ("pending", "Ожидает начала"),
    ]
    
    title = models.TextField(max_length=50, verbose_name="Название игры")
    about = models.TextField(blank=True, verbose_name="Об игре")
    rules = models.TextField(blank=True, verbose_name="Правила игры")
    max_players = models.PositiveIntegerField(validators=[
        MinValueValidator(1, "Должен быть хотя бы один игрок"),
        MaxValueValidator(100, "В игре не может быть больше 100 игроков")
        ], verbose_name="Количество игроков")
    players = models.ManyToManyField(User, through="GameParticipant", related_name="games", verbose_name="Игроки")
    characters = models.ManyToManyField(Character, related_name="games", verbose_name="Персонажи в игре")
    locations = models.ManyToManyField(Location, related_name="games", verbose_name="Локации в игре")
    status = models.CharField(choices=STATUS_CHOICES, default="pending", verbose_name="Статус игры")
    invite_code = models.CharField(max_length=20, blank=True, verbose_name="Код для приглашения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания игры")
    
    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
    
    def __str__(self):
        return self.title

class CharactersItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="characters_items", verbose_name="Этот предмет")
    owner = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="charcters_items", verbose_name="Владелец предмета")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="characters_items", verbose_name="Предмет в игре")
    
    class Meta:
        verbose_name = "Предмет персонажа"
        verbose_name_plural = "Предметы персонажа"
    
    def __str__(self):
        return f"{self.item.name} у персонажа {self.owner.name}"


class GameParticipant(models.Model):
    ROLES_CHOICES = [
        ("gm", "Мастер"),
        ("moderator", "Модератор"),
        ("player", "Игрок"),
        ("spectator", "Наблюдатель"),
    ]
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра")
    player = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Игрок")
    role = models.CharField(choices=ROLES_CHOICES, default="player", verbose_name="Роль в игре")
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата присоединения к игре")
    
    class Meta:
        verbose_name = "Участник игры"
        verbose_name_plural = "Участники игры"
    
    def __str__(self):
        return f"{self.player.username} в игре \"{self.game.title}\""


class Post(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="posts", verbose_name="Игра")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Пользователь")
    character = models.ForeignKey(Character, blank=True, null=True, on_delete=models.SET_NULL, related_name="posts", verbose_name="Персонаж")
    content = models.TextField(max_length=4000, verbose_name="Содержание")
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="replies", verbose_name="Ответ на пост")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    
    def get_short_content(self):
        if len(self.content) > 16:
            return self.content[:13] + "..."
        return self.content
    
    def __str__(self):
        return self.get_short_content()


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications", verbose_name="Пользователь")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="notifications", verbose_name="Пост")
    character = models.ForeignKey(Character, blank=True, null=True, on_delete=models.CASCADE, related_name="notifications", verbose_name="Персонаж")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="notifications", verbose_name="Игра")
    title = models.TextField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(max_length=4000, verbose_name="Содержание")
    type = models.CharField(max_length=50, verbose_name="Тип")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата получения")
    expires_at = models.DateTimeField(default=get_the_next_day(), verbose_name="Дата истечения") 
    
    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"
    
    def get_short_content(self):
        if len(self.content) > 16:
            return self.content[:13] + "..."
        return self.content
    
    def __str__(self):
        return self.get_short_content()
