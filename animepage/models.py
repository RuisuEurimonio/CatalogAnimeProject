from django.db import models

class TypeChoices(models.TextChoices):
    ANIME = 'AN', 'Anime'
    PELICULA = "PE", "Pelicula"
    OVA = "OV", "Ova"

class Genre(models.Model):
    name = models.CharField(max_length=15, unique=True)
    prefix = models.CharField(max_length= 5, unique= True)
    description = models.CharField(max_length=200, unique = True)

class Status(models.Model):
    name = models.CharField(max_length=15, unique=True)
    color = models.CharField(max_length=7, unique=True)

class Anime(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateField()
    main_genre = models.ForeignKey(Genre, on_delete=models.PROTECT, default=1)
    description = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=2000, default="no_image")
    type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        default=TypeChoices.ANIME
    )

    statusRef = models.ForeignKey(Status, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return f"{self.name}"

class Character(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=2000, default="no_image")

    def __str__(self):
        return f"{self.name}"
    
class Vote(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    observation = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.name}"
    

