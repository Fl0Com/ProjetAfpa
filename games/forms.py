from django.forms import ModelForm, FileInput, EmailInput, TextInput, DateInput
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class PlayerForm(ModelForm):
    class Meta :
        model = Player
        fields = ('avatar', 'dateNaissance')
        widgets = {
            'dateNaissance': DateInput(attrs={
                'type':"date", 
                'class':"input-xlarge"
                              }),
            'avatar': FileInput(attrs={
                'type':"file", 
                'placeholder':"Nom",
                'class':"btn btn-outline-primary"
                              })
            
        }

class SignUpForm1(ModelForm):
    class Meta:
        model = User
        fields = ('last_name','first_name','email')
        widgets = {
            'last_name': TextInput(attrs={
            'class':"input-xlarge",
            'placeholder':"Nom"
                              }),
            'first_name': TextInput(attrs={
            'placeholder':"Prénom",
            'class':"input-xlarge"
                              }),
            'email': EmailInput(attrs={
            'placeholder':"Email",
            'class':"input-xlarge"
                              })
            
        }


class  SignUpForm2(forms.Form):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(max_length=150)
    password2 = forms.CharField(max_length=150)