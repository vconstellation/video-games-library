from django import forms
from .models import GamesCollection
from users.models import ProfileGamesCollection, GamesReviews

class GamesCollectionForm(forms.ModelForm):
    class Meta:
        model = GamesCollection
        fields = '__all__'

class GamesCollectionAddForm(forms.ModelForm):
    class Meta:
        model = ProfileGamesCollection
        fields = []

class GamesReviewForm(forms.ModelForm):
    score_range = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]

    class Meta:
        model = GamesReviews
        fields = ['review', 'review_score']

    review_score = forms.ChoiceField(choices = score_range,
                                                    widget=forms.RadioSelect)