from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def MyHome(request) :
    return render(request, 'QatarWorldCup/base.html')

def Intro(request) :
    return render(request, 'QatarWorldCup/intro.html')