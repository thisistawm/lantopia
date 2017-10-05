from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Profile

#def profile(request):
#    template = loader.get_template('core/profile.html')
#    return HttpResponse(template.render(context, request))

def profile(request):
    return render(request, 'core/profile.html')
