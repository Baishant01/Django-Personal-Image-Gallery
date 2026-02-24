
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ImagePost

class RegisterForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ImagePostForm (forms.ModelForm):
    class Meta:
        model = ImagePost
        fields= ['image']
    