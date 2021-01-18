from django import forms
from .models import GamesCollection

class GamesCollectionForm(forms.ModelForm):
    class Meta:
        model = GamesCollection
        fields = '__all__'