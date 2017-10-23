from django.contrib.auth.models import User
from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ('team_name', 'member1', 'member2', 'crypts_wave', 'crypts_remaining')
