"""lantopia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .forms import CustomAuthForm
from core import views

handler404 = views.page_not_found

urlpatterns = [
    url(r'^home/$', views.homeInfo, name='homeInfo'),
    url(r'^profile/', include('core.urls')),
    url(r'^games/$', views.games, name='games'),
    url(r'^players/$', views.players, name='players'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^polls/', include('polls.urls')),
    url(r'^picks/', include('picks.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login, name='login', kwargs={"authentication_form":CustomAuthForm}),
    url(r'^$', auth_views.login, name='login', kwargs={"authentication_form":CustomAuthForm}),
    url(r'^logout/$', auth_views.logout, {'next_page':'/login'}, name='logout'),
    url(r'^scores/', include('scores.urls')),
]