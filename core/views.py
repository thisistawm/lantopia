from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Profile
from .forms import ProfileForm

#def profile(request):
#    return render(request, 'core/profile.html')

#def profile(request):
#	form = ProfileForm()
#	return render(request, 'core/profile.html', {'form': form})

def updateProfile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST,  instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'core/profile.html', {
    	'profile_form': profile_form
    })