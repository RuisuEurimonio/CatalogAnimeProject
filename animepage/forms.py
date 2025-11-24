from django import forms
from .models import Status, Genre, Anime

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["name", "color"]
        labels = {
            "name": "Estado",
            "color": "Color"
        }
        widgets = {
            "color": forms.TextInput(attrs={"type": "color"})
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name", "prefix", "description"]
        labels = {
            "name" : "nombre",
            "prefix" : "Prefijo",
            "description" : "descripcion"
        }

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ["name","date", "main_genre", "description", "img_url", "type", "statusRef"]
        labels= {
            "name": "Nombre",
            "date": "Fecha",
            "main_genre": "Genero principal",
            "description": "Descripción",
            "img_url": "Imagen url",
            "type": "Tipo",
            "statusRef": "Estado"
        }
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }