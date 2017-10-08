from django.shortcuts import render
from django.contrib.auth.models import User

from core.models import Profile


def index(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/index.html', {'all_users': all_users})

def songs(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/songs.html', {'all_users': all_users})
