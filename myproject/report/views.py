from django.shortcuts import render
from django.http import HttpResponse
import os
import xml.dom.minidom
# Create your views here.
def getAttr(path,ele,attr):
   dom = xml.dom.minidom.parse(path + '/test_result.xml')
   root = dom.documentElement
   Ele = root.getElementsByTagName(ele)
   Attr = Ele[0].getAttribute(attr)
   return Attr

def home(request):
    passCounts = []
    rootPath = '//10.75.10.81/Share/EVW/CTS/EVW_V0.33B'
    dirs = os.listdir(rootPath)
    path = rootPath + '/' + dirs[0] + '/results'
    subDir = os.listdir(path)
    subPath = path + '/' + subDir[0]
    #dom = xml.dom.minidom.parse(subPath + '/test_result.xml')
    #root = dom.documentElement
    #Build = root.getElementsByTagName('Build')
    Fingerprint = getAttr(subPath,'Build','build_fingerprint')
    for i in range(len(dirs)):
        testPath = rootPath + '/' + dirs[i-1] + '/results'
        print('now we are in ' + str(testPath))
        resultPath = testPath + '/' + os.listdir(testPath)[0]

    return render(request, 'home.html',{'dirs':dirs,'Fingerprint':Fingerprint,'rootPath':rootPath})
