from django import forms
from .models import Status, Genre

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