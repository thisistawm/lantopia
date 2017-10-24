from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.caps, name='caps'),
    url(r'^crypts/$', views.crypts, name='crypts'),
    url(r'^caps/$', views.caps, name='caps'),
]