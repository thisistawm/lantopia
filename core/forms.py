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
        fields = ('unpacked', 'setup', 'connected')
        widgets = {
            'unpacked': forms.CheckboxInput(attrs={'name': 'todoUpdateButton', 'onclick':'this.form.submit();'}),
            'setup': forms.CheckboxInput(attrs={'name': 'todoUpdateButton', 'onclick':'this.form.submit();'}),
            'connected': forms.CheckboxInput(attrs={'name': 'todoUpdateButton', 'onclick':'this.form.submit();'}),
        }
