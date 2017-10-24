from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.games, name='games'),
    url(r'^songs/$', views.songs, name='songs'),
    url(r'^games/$', views.games, name='games'),
    url(r'^movies/$', views.movies, name='movie'),
    url(r'^tv/$', views.tv, name='tv'),
]