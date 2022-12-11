from django import forms
from django.forms import ModelForm
from .models import Post,Ipe
from django.contrib.auth.forms import UserCreationForm

class FormPost(ModelForm):
    class Meta:
        model = Post
        fields=['titulo','descripcion','imagen','url']

class IpeForm(ModelForm):
    class Meta:
        model = Ipe
        fields=['ipe']


class CustomUserForm(UserCreationForm):
    pass
