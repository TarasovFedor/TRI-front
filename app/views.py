from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Character, Game

from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.urls import reverse

import rstr


User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = "Допустимы буквы (кириллица, латиница), цифры и спец. символы @.+-_"
        self.fields["password1"].help_text = "Минимальная длина пароля - 8 символов, должны содержаться буквы и цифры"
        self.fields["password2"].help_text = "Повторите пароль"

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("app:menu")
    else:
        form = RegisterForm()
    return render(request, "auth_user/register.html", { "form": form })

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("app:menu")
    else:
        form = LoginForm()
    
    return render(request, "auth_user/login.html", { "form": form })

def user_logout(request):
    logout(request)
    return redirect("app:menu")


def characters_list(request):
    characters = Character.objects.all().select_related("location")
    return render(request, "charList.vue", { "chars": characters })

@login_required
def my_characters_list(request):
    characters = Character.objects.filter(Q(owner=request.user)).\
        select_related("location")
    return render(request, "charList.vue", { "chars": characters })

@login_required
def character_create(request):
    if request.method == "POST":
        new_name = request.POST.get("name")
        new_about = request.POST.get("about")
        new_status = request.POST.get("status")
        new_characteristics = request.POST.get("characteristics")
        new_picture = request.FILES.get("picture")
        
        if Character.objects\
            .filter(Q(name=new_name) & Q(about=new_about)).exists():
            return render(request, "charCreate.vue", { "errors": "Такой персонаж уже существует" })
        
        character = Character.objects.create(
            name = new_name,
            about = new_about,
            status = new_status,
            characteristics = new_characteristics,
            picture=new_picture,
        )
        
        return redirect("app:char", pk=character.pk)
    return render(request, "charCreate.vue")

@login_required
def character_edit(request, pk):
    character = get_object_or_404(Character, pk=pk)
    
    if request.method == "POST":
        character.name = request.POST.get("name")
        character.about = request.POST.get("about")
        character.status = request.POST.get("status")
        character.characteristics = request.POST.get("characteristics")
        character.picture = request.FILES.get("picture")
        character.save()
        
        return redirect("app:char", pk-character.pk)
    return render(request, "charEdit.vue", { "character": character })

@login_required
def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    character.delete()
    return redirect("app:chars")

def character_about(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render("character.vue", { "character": character })

# Отсюда добавить урлы
def game_conponent(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, "gameComponent.vue", { "game": game })

def game_search(request):
    query = request.GET.get("query", "").strip()
    games = Game.objects.filter(
        Q(title__icontains=query) | Q(about__icontains=query) 
    ).distinct().order_by("name")
    
    return render(request, "gameSearch.vue", { "games": games })

@login_required
def game_create(request):
    if request.method == "POST":
        new_title = request.POST.get("title")
        new_about = request.POST.get("about")
        new_rules = request.POST.get("rules")
        new_max_players = request.POST.get("max_players")
        # added_locations = request.POST.get("locations")
        new_status = request.POST.get("status")
        
        if Game.objects.filter(Q(title=new_title)).exists():
            return render(request, "gameCreate.vue", { "errors": "Игра с таким названием уже существует" })
        
        character = Character.objects.create(
            title = new_title,
            about = new_about,
            rules = new_rules,
            max_players = new_max_players,
            status = new_status,
            invite_code = rstr.xeger(r'[A-Z0-9]{4}-[A-Z0-9]{4}')
        )
        
        return redirect("app:games", pk=character.pk)
    return render(request, "gameCreate.vue")

# Дальше не доделал
# @login_required
# def game_edit(request, pk):
#     character = get_object_or_404(Character, pk=pk)
    
#     if request.method == "POST":
#         character.name = request.POST.get("name")
#         character.about = request.POST.get("about")
#         character.status = request.POST.get("status")
#         character.characteristics = request.POST.get("characteristics")
#         character.picture = request.FILES.get("picture")
#         character.save()
        
#         return redirect("app:char", pk-character.pk)
#     return render(request, "charEdit.vue", { "character": character })

# @login_required
# def game_delete(request, pk):
#     character = get_object_or_404(Character, pk=pk)
#     character.delete()
#     return redirect("app:chars")
