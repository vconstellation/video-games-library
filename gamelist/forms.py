from django import forms
from .models import GamesCollection
from users.models import ProfileGamesCollection

class GamesCollectionForm(forms.ModelForm):
    class Meta:
        model = GamesCollection
        fields = '__all__'

class GamesCollectionAddForm(forms.ModelForm):
    class Meta:
        model = ProfileGamesCollection
        fields = []