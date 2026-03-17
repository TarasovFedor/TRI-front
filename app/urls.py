from django.urls import path
from . import views
from . import api_views


app_name = "app"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    
    path("chars/", views.characters_list, name="chars"),
    path("chars/my/", views.my_characters_list, name="chars"),
    path("chars/create/", views.character_about, name="chars"),
    path("chars/<int:pk>/edit", views.character_edit, name="char_edit"),
    path("chars/<int:pk>/delete", views.character_delete, name="char_delete"),
    path("chars/<int:pk>/", views.character_about, name="char"),
    
]
