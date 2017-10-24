from django.contrib.auth.models import User
from django import forms
from .models import Team, TeamMember

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ('name', 'crypts_wave', 'crypts_remaining')