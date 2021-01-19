from django import forms
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from crispy_forms.bootstrap import InlineCheckboxes

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'review', 'game', 'avatar']
       # fields = '__all__'

class ProfileGameCollectionUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['game']
        widgets = {
            'game': forms.CheckboxSelectMultiple()
        }

