from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class CustomAuthForm(AuthenticationForm):
	    username = forms.CharField(widget=TextInput(attrs={'class':'loginInput','placeholder':'username'}))
	    password = forms.CharField(widget=PasswordInput(attrs={'class':'loginInput','placeholder':'password'}))