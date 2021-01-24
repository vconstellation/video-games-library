from django import forms
from .models import Profile

platform = [
        ('PC', 'PC'),
        ('XBOX', 'XBOX')
        ]

class ProfileUpdateForm(forms.ModelForm):
    platform = [
            ('PC', 'PC'),
            ('XBOX', 'XBOX')
            ]

    platform_checkbox = forms.MultipleChoiceField(choices = platform, widget = forms.CheckboxSelectMultiple())

    class Meta:
        model = Profile
        exclude = ['user', 'review', 'game', 'platform_used']
       # fields = '__all__

class ProfileGameCollectionUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['game']
        widgets = {
            'game': forms.CheckboxSelectMultiple()
        }

