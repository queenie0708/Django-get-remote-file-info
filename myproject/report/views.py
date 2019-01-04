from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.
def home(request):
    path = '//10.75.10.81/Share/EVW/CTS/EVW_V0.33B'
    dirs = os.listdir(path)
    return render(request, 'home.html',{'dirs':dirs})
