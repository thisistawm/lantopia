from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.template import Context

from core.models import Profile
from .models import Team, TeamMember

from .forms import TeamForm

def crypts(request):
    if request.method == "POST" and 'createTeamButton' in request.POST:
        form = TeamForm(request.POST)
        new_team = form.save()
        new_member1 = TeamMember(user=request.user, team=new_team)
        new_member1.save()
        team_mate = User.objects.get(username=request.POST['team-mate'])
        new_member2 = TeamMember(user=team_mate, team=new_team)
        new_member2.save()
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    all_teams = Team.objects.all().order_by('-crypts_wave', 'crypts_remaining')
    return render(request, 'scores/crypts.html', {'all_users': all_users, 'all_teams': all_teams})

def caps(request):
    all_users = User.objects.all().exclude(username="admin").order_by('-profile__caps')
    return render(request, 'scores/caps.html', {'all_users': all_users})
