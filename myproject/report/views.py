from django.shortcuts import render
from django.http import HttpResponse
import os
import xml.dom.minidom
# Create your views here.
def home(request):
    rootPath = '//10.75.10.81/Share/EVW/CTS/EVW_V0.33B'
    dirs = os.listdir(rootPath)
    path = rootPath + '/' + dirs[0] + '/results'
    subDir = os.listdir(path)
    subPath = path + '/' + subDir[0]
    dom = xml.dom.minidom.parse(subPath + '/test_result.xml')
    root = dom.documentElement
    Build = root.getElementsByTagName('Build')
    Fingerprint = Build[0].getAttribute('build_fingerprint')
    return render(request, 'home.html',{'dirs':dirs,'Fingerprint':Fingerprint,'rootPath':rootPath})
