from django import forms
from .models import Profile, ProfileGamesCollection, Platform


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['avatar', 'background_image', 'nickname', 'bio', 'platform_used', 'steam_link']

    platform_used = forms.ModelMultipleChoiceField(queryset=Platform.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple)


class ProfileGameCollectionUpdate(forms.ModelForm):
    class Meta:
        model = ProfileGamesCollection
        fields = ['games_collection', 'currently_playing', 'finished']


class ProfileGameCollectionSingleItemUpdate(forms.ModelForm):
    class Meta:
        model = ProfileGamesCollection
        fields = ['currently_playing', 'finished']
    

