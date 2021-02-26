from django import forms
from .models import GamesCollection, GamesReviews
from users.models import ProfileGamesCollection

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
        fields = ['review', 'story_score', 'music_score', 'gameplay_score', 'visual_score']

    visual_score = forms.ChoiceField(choices = score_range,
                                                    widget=forms.RadioSelect)
    music_score = forms.ChoiceField(choices = score_range,
                                                    widget=forms.RadioSelect)
    story_score = forms.ChoiceField(choices = score_range,
                                                    widget=forms.RadioSelect)
    gameplay_score = forms.ChoiceField(choices = score_range,
                                                    widget=forms.RadioSelect)