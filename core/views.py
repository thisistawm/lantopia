from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Profile, Todo, HomeInfo
from .forms import ProfileForm, TodoForm
from lantopia.forms import SignupForm, CustomPasswordChangeForm

@login_required
def profile(request):
    if request.method == "POST" and 'profileUpdateButton' in request.POST:
        profile_form = ProfileForm(request.POST,  instance=request.user.profile)
        password_form = CustomPasswordChangeForm(request.user)
        todo_form = TodoForm(instance=request.user.todo)
        if profile_form.is_valid():
            profile_form.save()
    elif request.method == "POST" and 'passwordUpdateButton' in request.POST:
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        todo_form = TodoForm(instance=request.user.todo)
        profile_form = ProfileForm(instance=request.user.profile)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
        else:
            return render(request, 'core/profile.html', {
            'password_form': password_form,
            'profile_form': profile_form,
            'todo_form': todo_form
             })
    elif request.method == "POST":
        todo_form = TodoForm(request.POST,  instance=request.user.todo)
        password_form = CustomPasswordChangeForm(request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        if todo_form.is_valid():
            todo_form.save()
    else:
        password_form = CustomPasswordChangeForm(request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        todo_form = TodoForm(instance=request.user.todo)
    todo_count = 0
    checklist_done = False
    for z in todo_form:
        if z.value == False:
            todo_count += 1
    if request.method =="POST":
        return HttpResponseRedirect('/profile', {
            'password_form': password_form,
            'profile_form': profile_form,
            'todo_form': todo_form,
            'checklist_done': checklist_done,
            'todo_count': todo_count
        })
    else:
        return render(request, 'core/profile.html', {
            'password_form': password_form,
            'profile_form': profile_form,
            'todo_form': todo_form,
            'checklist_done': checklist_done,
            'todo_count': todo_count
        })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/profile')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def homeInfo(request):
    info = HomeInfo.objects.filter(post_time__lte=timezone.now()).order_by('post_time')
    return render(request, 'core/home.html', {'info': info} )

@login_required
def games(request):
    return render(request, 'core/games.html')

@login_required
def players(request):
    return render(request, 'core/players.html')

def page_not_found(request):
    response = "<h1>no findy</h1>"
    return HttpResponse(response)
