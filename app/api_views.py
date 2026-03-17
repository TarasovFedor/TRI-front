from rest_framework import generics
from .models import User, Item, Location, Character, Game, GameParticipant, Post, Notification
from .serializers import UserSerializer, ItemSerializer, LocationSerializer, CharacterSerializer, GameSerializer, GameParticipantSerializer, PostSerializer, NotificationSerializer
from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItemListAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all().order_by("-created_at")
    serializer_class = ItemSerializer

class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class LocationListAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all().order_by("-created_at")
    serializer_class = LocationSerializer

class LocationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CharacterListAPIView(generics.ListCreateAPIView):
    queryset = Character.objects.all().order_by("-created_at")
    serializer_class = CharacterSerializer

class CharacterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class GameListAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all().order_by("-created_at")
    serializer_class = GameSerializer

class GameDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameParticipantListAPIView(generics.ListCreateAPIView):
    queryset = GameParticipant.objects.all().order_by("-created_at")
    serializer_class = GameParticipantSerializer

class GameParticipantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameParticipant.objects.all()
    serializer_class = GameParticipantSerializer


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class NotificationListAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all().order_by("-created_at")
    serializer_class = NotificationSerializer

class NotificationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer