from django import forms
from .models import Profile, ProfileGamesCollection, Platform

platform = [
        ('PC', 'PC'),
        ('XBOX', 'XBOX')
        ]

class ProfileUpdateForm(forms.ModelForm):
    # platform = [
    #         ('PC', 'PC'),
    #         ('XBOX', 'XBOX')
    #         ]

    #platform_checkbox = forms.MultipleChoiceField(choices = platform, widget = forms.CheckboxSelectMultiple())

    
    class Meta:
        model = Profile
        fields = ['avatar', 'nickname', 'bio', 'platform_used', 'steam_link']
        #exclude = ['user', 'review', 'game', 'slug']

    platform_used = forms.ModelMultipleChoiceField(queryset=Platform.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple)
       # fields = '__all__

class ProfileGameCollectionUpdate(forms.ModelForm):
    class Meta:
        model = ProfileGamesCollection
        fields = ['games_collection', 'currently_playing', 'finished']
        # widgets = {
        #     'games_collection': forms.CheckboxSelectMultiple()
        # }

