from rest_framework import serializers # pyright: ignore[reportMissingImports]
from .models import User, Item, Location, Character, Game, GameParticipant, Post, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "is_admin", "created_at")
    

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "about", "characteristics", "creator__name", "created_at")


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name", "about", "creator__name", "rules", "items__name", "created_at")


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "name", "about", "characteristics", "owner__name", "at_location__name", "status", "created_at", "updated_at")


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("id", "title", "about", "rules", "status", "max_players", "players__name", "characters__name", "locations__name", "invite_code", "created_at")


class GameParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameParticipant
        fields = ("id", "game__title", "player__username", "role", "joined_at")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "game__title", "user__username", "character__name", "content", "reply_to__id", "created_at", "updated_at")


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("id", "user__username", "post__id", "title", "content", "character__name", "game__title", "type", "is_read", "created_at", "expires_at")


