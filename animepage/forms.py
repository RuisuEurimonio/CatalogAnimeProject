from django import forms
from .models import Status

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
