from django.contrib.auth.models import User
from django import forms
from .models import Profile, Todo
from django.forms.widgets import CheckboxInput

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('game', 'song', 'movie', 'tv')

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('sayHi', 'getGames', 'checkDrinks', 'makePicks', 'doRevel')
        widgets = {
            'sayHi': forms.CheckboxInput(attrs={'name': 'todoUpdateButton', 'onclick':'this.form.submit();'}),
            'getGames': forms.CheckboxInput(attrs={'name': 'todoUpdateButton', 'onclick':'this.form.submit();'}),
            'checkDrinks': forms.CheckboxInput(attrs={'name': 'todoUpdateButton', 'onclick':'this.form.submit();'}),
            'makePicks': forms.CheckboxInput(attrs={'name': 'todoUpdateButton', 'onclick':'this.form.submit();'}),
            'doRevel': forms.CheckboxInput(attrs={'name': 'todoUpdateButton', 'onclick':'this.form.submit();'}),
        }
        labels = {
            "sayHi":"Say hi to everyone",
            "getGames":"Get all games",
            "checkDrinks":"Check out food & drink",
            "makePicks":"Provide recommendations",
            "doRevel":"Revel",
        }