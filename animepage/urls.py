from django.urls import path

from . import views

app_name= "anime"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:anime_id>/", views.info, name="info"),
    path("create", views.create, name="create"),
    path("vote", views.vote, name="vote"),
    path("vote/<int:id>/delete", views.deleteVote, name="deleteVote"),
    path("votes", views.votes, name="votes"),
    path("<int:anime_id>/delete", views.deleteAnime, name="deleteAnime"),
    path("<int:anime_id>/character/<int:character_id>", views.character, name="character"),
    path("<int:anime_id>/character/create", views.createCharacter, name="createCharacter"),
    path("<int:anime_id>/character/<int:character_id>/delete", views.deleteCharacter, name="deleteCharacter"),
    path("<int:anime_id>/character/<int:character_id>/edit", views.editCharacter, name="infoCharacters"),
]