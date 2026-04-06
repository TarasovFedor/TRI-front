from rest_framework import serializers # pyright: ignore[reportMissingImports]
from .models import User, Item, Location, Character, Game, GameParticipant, Post, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "is_admin", "created_at")
    

class ItemSerializer(serializers.ModelSerializer):
    creators_name = serializers.CharField(source="creator.username")
    class Meta:
        model = Item
        fields = ("id", "name", "about", "characteristics", "creators_name", "created_at")


class LocationSerializer(serializers.ModelSerializer):
    creators_name = serializers.CharField(source="creator.username")
    items_name = serializers.StringRelatedField(many=True, source="items.name")
    class Meta:
        model = Location
        fields = ("id", "name", "about", "creators_name", "rules", "items_name", "created_at")


class CharacterSerializer(serializers.ModelSerializer):
    owners_name = serializers.CharField(source="owner.username")
    location_name = serializers.CharField(source="at_location.name")
    class Meta:
        model = Character
        fields = ("id", "name", "about", "characteristics", "owners_name", "location_name", "status", "created_at", "updated_at")


class GameSerializer(serializers.ModelSerializer):
    players_name = serializers.StringRelatedField(many=True, source="players.username")
    characters_name = serializers.StringRelatedField(many=True, source="characters.name")
    locations_name = serializers.StringRelatedField(many=True, source="locations.name")
    class Meta:
        model = Game
        fields = ("id", "title", "about", "rules", "status", "max_players", "players_name", "characters_name", "locations_name", "invite_code", "created_at")


class GameParticipantSerializer(serializers.ModelSerializer):
    game_title = serializers.CharField(source="game.title")
    player_username = serializers.CharField(source="player.username")
    class Meta:
        model = GameParticipant
        fields = ("id", "game_title", "player_username", "role", "joined_at")


class PostSerializer(serializers.ModelSerializer):
    game_title = serializers.CharField(source="game.title")
    user_username = serializers.CharField(source="user.username")
    character_name = serializers.CharField(source="character.name")
    reply_to_id = serializers.IntegerField(source="reply_to.id", allow_null=True)
    class Meta:
        model = Post
        fields = ("id", "game_title", "user_username", "character_name", "content", "reply_to_id", "created_at", "updated_at")


class NotificationSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source="user.username")
    post_id = serializers.IntegerField(source="post.id", allow_null=True)
    character_name = serializers.CharField(source="character.name")
    game_title = serializers.CharField(source="game.title")
    class Meta:
        model = Notification
        fields = ("id", "user_username", "post_id", "title", "content", "character_name", "game_title", "type", "is_read", "created_at", "expires_at")


