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

def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        prof = form.save(commit=False)
        prof.save()
    else:
        form = ProfileForm()
    return render(request, 'core/profile.html', {'form': form})