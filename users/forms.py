from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'review', 'game', 'avatar']
       # fields = '__all__'

class ProfileGameCollectionUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['game']