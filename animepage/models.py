from django.db import models

class GenreChoices(models.TextChoices):
    ACCION = 'ACC', 'Acción'
    COMEDIA = 'COM', 'Comedia'
    DRAMA = 'DRM', 'Drama'
    FANTASIA = 'FAN', 'Fantasía'

class StatusChoices(models.TextChoices):
    EMISION = 'EM', 'Emisión'
    PROXIMAMENTE = 'PROX', "Proximamente"
    FINALIZADO = 'FIN', "Finalizado"

class TypeChoices(models.TextChoices):
    ANIME = 'AN', 'Anime'
    PELICULA = "PE", "Pelicula"
    OVA = "OV", "Ova"

class Anime(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateField()
    main_genre = models.CharField(
        choices=GenreChoices.choices,
        default=GenreChoices.ACCION
    )
    description = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=2000, default="no_image")
    status = models.CharField(
        choices=StatusChoices.choices,
        default=StatusChoices.FINALIZADO
    )
    type = models.CharField(
        choices=TypeChoices.choices,
        default=TypeChoices.ANIME
    )

    def __str__(self):
        return f"{self.name}";

class Character(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=2000, default="no_image")

    def __str__(self):
        return f"{self.name}"