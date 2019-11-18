from django import forms
from .models import VideoModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VideoModelForm(forms.ModelForm):
    thumbnail = forms.ImageField(label='thumbnail')

    class Meta:
        model = VideoModel
        fields = ('videofile', 'title', 'description', 'tags', 'categories', 'thumbnail', 'duration')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ('email',)
