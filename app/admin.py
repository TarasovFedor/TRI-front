from django.contrib import admin
from app.models import User, Item, Location, Character, Game, CharactersItem, GameParticipant, Post, Notification
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _
from django.db.models import F, Q, Min, Subquery, OuterRef, Count


class UsersGamesInline(admin.TabularInline):
    model = GameParticipant
    extra = 1

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "is_admin",
        "about",
        "avatar_preview",
        "created_at",
    )
    
    list_filter = ("is_admin", "created_at")
    search_fields = ("username", "email")
    list_display_links = ("username", )
    readonly_fields = ("is_admin", "created_at")
    inlines = [UsersGamesInline]
    
    @admin.display(description="Превью аватара")
    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html("<img src='{}' style='width: 50px; height: 50px;'/>", obj.avatar.url)
        return "..."
    
    def get_readonly_fields(self, request, obj = None):
        return ("created_at", ) if not obj else self.readonly_fields


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_about",
        "short_characteristics",
        "creators_username",
        "location_name",
        "created_at",
    )
    
    list_filter = ("creator", "created_at")
    search_fields = ("name", "about", "creators_username", "location_name")
    list_display_links = ("name", )
    readonly_fields = ("created_at", )
    
    def get_queryset(self, request):
        return super().get_queryset(request).\
            select_related("creator").prefetch_related("locations").annotate(
                creators_username=F("creator__username"),
                current_location=F("locations__name"),
            )
    
    @admin.display(description="Создатель предмета")
    def creators_username(self, obj):
        return obj.creators_username

    @admin.display(description="Локация предмета")
    def location_name(self, obj):
        return obj.current_location
    
    @admin.display(description="Вкратце о предмете")
    def short_about(self, obj):
        return (obj.about[:50] + "...") if len(obj.about) > 50 else obj.about
    
    @admin.display(description="Вкратце о характеристиках")
    def short_characteristics(self, obj):
        return (obj.characteristics[:50] + "...") if len(obj.characteristics) > 50 else obj.characteristics


# class ItemsAtLocationInline(admin.TabularInline):
#     model = Location.items.through
#     extra = 1

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "creators_username",
        "short_about",
        "short_rules",
        "picture_preview",
    )
    
    list_filter = ("creator", )
    search_fields = ("name", "about")
    list_display_links = ("name", )
    # inlines = [ItemsAtLocationInline]
    
    def get_queryset(self, request):
        return super().get_queryset(request).\
            select_related("creator").annotate(
                creators_username=F("creator__username"),
            )
    
    @admin.display(description="Создатель локации")
    def creators_username(self, obj):
        return obj.creators_username
    
    @admin.display(description="Вкратце о локации")
    def short_about(self, obj):
        return (obj.about[:50] + "...") if len(obj.about) > 50 else obj.about
    
    @admin.display(description="Правила вкратце")
    def short_rules(self, obj):
        return (obj.rules[:50] + "...") if len(obj.rules) > 50 else obj.rules
    
    @admin.display(description="Превью локации")
    def picture_preview(self, obj):
        if obj.picture:
            return format_html("<img src='{}' style='width: 50px; height: 50px;'/>", obj.picture.url)
        return "..."


class CharactersItemsInline(admin.TabularInline):
    model = CharactersItem
    extra = 1

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_about",
        "picture_preview",
        "username",
        "status",
        "short_characteristics",
        "location",
        "created_at",
        "updated_at",
    )
    
    list_filter = ("created_at", "updated_at", "owner", "status")
    search_fields = ("name", "about", "owner")
    list_display_links = ("name", )
    raw_id_fields = ("owner", "at_location")
    readonly_fields = ("created_at", "owner")
    inlines = [CharactersItemsInline]
    
    def get_queryset(self, request):
        return super().get_queryset(request).\
            select_related("owner").select_related("at_location").annotate(
                owners_username=F("owner__username"),
                current_location=F("at_location__name"),
            )
    
    @admin.display(description="Владелец персонажа")
    def username(self, obj):
        return obj.owners_username

    @admin.display(description="Локация персонажа")
    def location(self, obj):
        return obj.current_location
    
    @admin.display(description="Вкратце о персонаже")
    def short_about(self, obj):
        return (obj.about[:50] + "...") if len(obj.about) > 50 else obj.about
    
    @admin.display(description="Вкратце о характеристиках")
    def short_characteristics(self, obj):
        return (obj.characteristics[:50] + "...") if len(obj.characteristics) > 50 else obj.characteristics
    
    @admin.display(description="Превью персонажа")
    def picture_preview(self, obj):
        if obj.picture:
            return format_html("<img src='{}' style='width: 50px; height: 50px;'/>", obj.picture.url)
        return "..."

    def get_readonly_fields(self, request, obj = None):
        return ("created_at", ) if not obj else self.readonly_fields


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "short_about",
        "short_rules",
        "master",
        "current_players_amount",
        "max_players",
        "status",
        "invite_code",
        "created_at",
    )
    
    list_filter = ("created_at", "max_players")
    search_fields = ("title", "about", "master")
    list_display_links = ("title", )
    readonly_fields = ("created_at", )
    
    inlines = [UsersGamesInline]
    
    def get_queryset(self, request):
        master_subquery = GameParticipant.objects.filter(
            game=OuterRef("pk"),
            role="gm"
        ).values("player")[:1]
        
        return super().get_queryset(request).\
            prefetch_related("players").annotate(
                master=Subquery(master_subquery),
                current_players_amount=Count("pk"),
            )
    
    @admin.display(description="Мастер игры")
    def master(self, obj):
        return obj.master

    @admin.display(description="Число игроков")
    def current_players_amount(self, obj):
        return obj.current_players_amount
    
    @admin.display(description="Вкратце об игре")
    def short_about(self, obj):
        return (obj.about[:50] + "...") if len(obj.about) > 50 else obj.about
    
    @admin.display(description="Правила вкратце")
    def short_rules(self, obj):
        return (obj.rules[:50] + "...") if len(obj.rules) > 50 else obj.rules


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "game_title",
        "username",
        "character_name",
        "short_content",
        "updated_at",
        "created_at",
    )
    
    list_filter = ("created_at", "updated_at")
    search_fields = ("game_title", "content", "username", "character_name")
    readonly_fields = ("updated_at", "created_at")
    raw_id_fields = ("game", "user", "character", "reply_to", )
    
    def get_queryset(self, request):
        return super().get_queryset(request).\
            select_related("game", "user", "character").annotate(
                game_title=F("game__title"),
                username=F("user__username"),
                character_name=F("character__name"),
            )
    
    @admin.display(description="Название игры")
    def game_title(self, obj):
        return obj.game_title

    @admin.display(description="Имя пользователя")
    def username(self, obj):
        return obj.username
    
    @admin.display(description="Имя персонажа")
    def character_name(self, obj):
        return obj.character_name
    
    @admin.display(description="Содержание вкратце")
    def short_content(self, obj):
        return (obj.content[:50] + "...") if len(obj.content) > 50 else obj.content


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "short_content",
        "type",
        "username",
        "is_read",
        "short_post_content",
        "character_name",
        "game_title",
        "created_at",
        "expires_at",
    )
    
    list_filter = ("type", "is_read", "created_at", "expires_at")
    search_fields = ("title", "content", "username", "game_title", )
    list_display_links = ("title", )
    readonly_fields = ("created_at", )
    raw_id_fields = ("user", "post", "character", "game", )
    
    def get_queryset(self, request):
        return super().get_queryset(request).\
            select_related("user", "post", "character", "game").annotate(
                username=F("user__username"),
                post_content=F("post__content"),
                character_name=F("character__name"),
                game_title=F("game__title")
            )
    
    @admin.display(description="Имя пользователя")
    def username(self, obj):
        return obj.username
    
    @admin.display(description="Текст поста вкратце")
    def short_post_content(self, obj):
        return (obj.post_content[:50] + "...") if len(obj.post_content) > 50 else obj.post_content
    
    @admin.display(description="Имя персонажа")
    def character_name(self, obj):
        return obj.character_name
    
    @admin.display(description="Название игры")
    def game_title(self, obj):
        return obj.game_title
    
    @admin.display(description="Содержание вкратце")
    def short_content(self, obj):
        return (obj.content[:50] + "...") if len(obj.content) > 50 else obj.content
    