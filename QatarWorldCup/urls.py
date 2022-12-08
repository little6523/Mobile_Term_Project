from django.urls import path

from . import views

app_name = 'QatarWorldCup'

urlpatterns = [
    path('', views.MyHome, name='MyHome'),
    path('/Intro', views.Intro, name='Intro'),
]