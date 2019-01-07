from django.shortcuts import render
from django.http import HttpResponse
import json
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
    rootPath = '//10.75.10.81/Share/Dynamo2/CTS/V0.500'
    dirs = os.listdir(rootPath)
    path = rootPath + '/' + dirs[0] + '/results'
    subDir = os.listdir(path)
    subPath = path + '/' + subDir[0]
    #dom = xml.dom.minidom.parse(subPath + '/test_result.xml')
    #root = dom.documentElement
    #Build = root.getElementsByTagName('Build')
    Fingerprint = getAttr(subPath,'Build','build_fingerprint')
    passCounts = []
    failedCounts = []
    Models = []
    for i in range(len(dirs)):
        testPath = rootPath + '/' + dirs[i-1] + '/results'
        print('now we are in ' + str(testPath))
        resultPath = testPath + '/' + os.listdir(testPath)[0]
        passCount = getAttr(resultPath,'Summary','pass')
        # failedCount = getAttr(resultPath,'Summary','failed')
        # modelDone = getAttr(resultPath,'Summary','models_done')
        # modelTotal = getAttr(resultPath,'Summary','models_total')
        # passCounts.append(passCount)
        # failedCounts.append(failedCount)
        # Models.append(modelDone + '/' + modelTotal)
    return render(request, 'home.html',{'dirs':json.dumps(dirs),'Fingerprint':Fingerprint,'rootPath':rootPath,'passCounts':json.dumps(passCount)s,'failedCounts':json.dumps(failedCounts)})
