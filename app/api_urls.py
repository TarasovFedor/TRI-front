from django.urls import path, include
from .api_views import UserListAPIView, UserDetailAPIView, ItemListAPIView, ItemDetailAPIView, LocationListAPIView, LocationDetailAPIView, CharacterListAPIView, CharacterDetailAPIView, GameListAPIView, GameDetailAPIView, GameParticipantListAPIView, GameParticipantDetailAPIView, PostListAPIView, PostDetailAPIView, NotificationListAPIView, NotificationDetailAPIView
from rest_framework.routers import DefaultRouter

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


# router = DefaultRouter()
# router.register("questions", QuestionViewSet, basename="api-questions")

urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="api_user_list"),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name="api_user_detail"),
    path("items/", ItemListAPIView.as_view(), name="api_item_list"),
    path("items/<int:pk>/", ItemDetailAPIView.as_view(), name="api_item_detail"),
    path("locations/", LocationListAPIView.as_view(), name="api_location_list"),
    path("locations/<int:pk>/", LocationDetailAPIView.as_view(), name="api_location_detail"),
    path("characters/", CharacterListAPIView.as_view(), name="api_character_list"),
    path("characters/<int:pk>/", CharacterDetailAPIView.as_view(), name="api_character_detail"),
    path("games/", GameListAPIView.as_view(), name="api_game_list"),
    path("games/<int:pk>/", GameDetailAPIView.as_view(), name="api_game_detail"),
    path("game-participants/", GameParticipantListAPIView.as_view(), name="api_game_participant_list"),
    path("game-participants/<int:pk>/", GameParticipantDetailAPIView.as_view(), name="api_game_participant_detail"),
    path("posts/", PostListAPIView.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="api_post_detail"),
    path("notifications/", NotificationListAPIView.as_view(), name="api_notification_list"),
    path("notifications/<int:pk>/", NotificationDetailAPIView.as_view(), name="api_notification_detail"),


    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # path("", include(router.urls)),
]
