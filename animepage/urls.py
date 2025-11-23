from django.urls import path

from . import views
from .views import Info, CreateAnime, CreateStatus, EditStatus, DeleteStatus, CreateGenre, EditGenre, DeleteGenre

app_name= "anime"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", Info.as_view(), name="info"),
    path("create", CreateAnime.as_view(), name="create"),
    path("vote", views.vote, name="vote"),
    path("vote/<int:id>/delete", views.deleteVote, name="deleteVote"),
    path("votes", views.votes, name="votes"),
    path("<int:anime_id>/delete", views.deleteAnime, name="deleteAnime"),
    path("<int:anime_id>/character/<int:character_id>", views.character, name="character"),
    path("<int:anime_id>/character/create", views.createCharacter, name="createCharacter"),
    path("<int:anime_id>/character/<int:character_id>/delete", views.deleteCharacter, name="deleteCharacter"),
    path("<int:anime_id>/character/<int:character_id>/edit", views.editCharacter, name="infoCharacters"),
    path("/config", views.config, name="config"),
    path("config/status/create", CreateStatus.as_view(), name="createStatus" ),
    path("config/status/edit/<int:pk>", EditStatus.as_view(), name="editStatus" ),
    path("config/status/delete/<int:pk>", DeleteStatus.as_view(), name="deleteStatus" ),
    path("config/genre/create", CreateGenre.as_view(), name="createGenre" ),
    path("config/genre/edit/<int:pk>", EditGenre.as_view(), name="editGenre" ),
    path("config/genre/delete/<int:pk>", DeleteGenre.as_view(), name="deleteGenre" ),
]