from django.shortcuts import render
from django.http import HttpRespons
import datetime


def home(request):
    return HttpRespons('welcome to home page')


def contact(request):
    return render(request,'hello4/ about.html')











# Create your views here.
