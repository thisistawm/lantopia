from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .models import Profile, Todo
from .forms import ProfileForm, TodoForm

#def profile(request):
#    return render(request, 'core/profile.html')

#def profile(request):
#	form = ProfileForm()
#	return render(request, 'core/profile.html', {'form': form})

def updateProfile(request):
    if request.method == "POST" and 'profileUpdateButton' in request.POST:
        password_form = PasswordChangeForm(request.user, request.POST)
        profile_form = ProfileForm(request.POST,  instance=request.user.profile)
        todo_form = TodoForm(instance=request.user.todo)
        if profile_form.is_valid():
            profile_form.save()
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
    elif request.method == "POST":
        todo_form = TodoForm(request.POST,  instance=request.user.todo)
        password_form = PasswordChangeForm(request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        if todo_form.is_valid():
            todo_form.save()
    else:
        password_form = PasswordChangeForm(request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        todo_form = TodoForm(instance=request.user.todo)
    return render(request, 'core/profile.html', {
        'password_form': password_form,
        'profile_form': profile_form,
        'todo_form': todo_form
    })