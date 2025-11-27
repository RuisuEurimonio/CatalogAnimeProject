from django.test import TestCase
from django.urls import reverse
from .models import Anime, Status, Genre
from datetime import date

class CreateAnime(TestCase):

    def setUp(self):
        # Crear género y status requeridos (porque tu modelo los exige)
        self.genre = Genre.objects.create(name="Fantasia", prefix="Fan", description = "With magic")
        self.status = Status.objects.create(name="En emisión", color = "#f3f0f4")

    def test_create(self):
        genre = Genre.objects.create(
            name = "Accion",
            prefix = "Acc",
            description = "Fight and more"
        )

        status = Status.objects.create(
            name = "Emisión",
            color = "#ffffff"
        )

        anime = Anime.objects.create(
            name="Bleach",
            date=date(2004, 10, 5),
            main_genre= genre,
            description="Shinigamis",
            type="ANIME",
            statusRef=status
        )

        self.assertEqual(str(anime), "Bleach")
        self.assertEqual(str(genre), "Accion")
        self.assertEqual(str(status), "Emisión")
        self.assertEqual(Anime.objects.count(), 1)
        self.assertEqual(Anime.objects.get(id=anime.id).name, "Bleach")

    def test_update(self):
        anime = Anime.objects.create(
            name="One Piece",
            date=date(1999, 10, 20),
            main_genre=self.genre,
            description="Piratas",
            img_url="img",
            type="Anime",
            statusRef=self.status
        )

        anime.name = "One Piece (Actualizado)"
        anime.save()

        updated = Anime.objects.get(id=anime.id)
        self.assertEqual(updated.name, "One Piece (Actualizado)")

    def test_delete_anime(self):
        anime = Anime.objects.create(
            name="Attack on Titan",
            date=date(2013, 4, 7),
            main_genre=self.genre,
            description="Titanes",
            img_url="img",
            type="Anime",
            statusRef=self.status
        )

        anime_id = anime.id
        anime.delete()

        self.assertFalse(Anime.objects.filter(id=anime_id).exists())