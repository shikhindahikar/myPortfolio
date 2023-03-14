from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('about.html', views.about, name = 'about'),
    path('projects.html', views.projects, name = 'projects'),
    path('music.html', views.music, name = 'music'),
]