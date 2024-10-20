from django.contrib.auth.models import User
from .models import Profile
from django.forms.models import ModelForm
from django.forms.widgets import FileInput
from django import forms 


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_img': FileInput(),
        }

    