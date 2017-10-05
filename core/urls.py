from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
]