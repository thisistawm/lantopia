from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from lantopia.forms import CustomAuthForm

from . import views

urlpatterns = [
    url(r'^$', views.updateProfile, name='profile'),
    url(r'^home/$', views.homeInfo, name='homeInfo'),
    url(r'^signup/$', views.signup, name='signup')
]