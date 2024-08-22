from django import forms
from django.contrib.auth.forms import UserCreationForm
from cakeapp.models import Login,Owner,Client,Cake,Category
from django.db import models

class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )
    class Meta:
        model=Login
        fields=('username','password1','password2')


class Ownerform(forms.ModelForm):
    class Meta:
        model=Owner
        exclude=('user',)

class Userform(forms.ModelForm):
    class Meta:
        model=Client
        exclude=('user',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'


class CakeForm(forms.ModelForm):
    class Meta:
        model=Cake
        fields='__all__'