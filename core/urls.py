from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.updateProfile, name='profile'),
    url(r'^home/$', views.homeInfo, name='homeInfo'),

]