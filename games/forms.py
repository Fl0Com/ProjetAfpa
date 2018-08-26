from django.forms import DateInput, EmailInput, FileInput, ModelForm, TextInput, PasswordInput
from django import forms

from .models import *


class PlayerForm(ModelForm):
    class Meta :
        model = Player
        fields = ('avatar', 'dateNaissance')
        widgets = {
            'dateNaissance': DateInput(attrs={
                'type':"date", 
                'class':"input-xlarge",
                'value':'player.dateNaissance'}),
            'avatar': FileInput(attrs={
                'type':"file", 
                'placeholder':"Nom",
                'class':"btn form-control-file"})            
        }

class SignUpForm1(ModelForm):
    class Meta:
        model = User
        fields = ('last_name','first_name','email')
        widgets = {
            'last_name': TextInput(attrs={
            'class':"input-xlarge",
            'placeholder':"Nom"}),
            'first_name': TextInput(attrs={
            'placeholder':"Prénom",
            'class':"input-xlarge"}),
            'email': EmailInput(attrs={
            'placeholder':"Email",
            'class':"input-xlarge"})            
        }


class  SignUpForm2(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={'class':'input-xlarge','placeholder': 'Votre Pseudo'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'input-xlarge','placeholder': 'Mot de Passe'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'input-xlarge','placeholder': 'Mot de Passe'}))
