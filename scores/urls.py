from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^crypts/$', views.crypts, name='crypts'),
]