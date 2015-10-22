#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from web_models import models

import urllib
import threading
# Create your views here.

def monitor_web(request):
    data = models.WebServer.objects.values("hostname","port","url","app")
    data_ = []

    for d in data:
        d["code"] = get_code(d["url"])

        data_.append(d)

    return render_to_response("monitor/monitor_web.html",{"data":data_})


def get_code(d):

    url = d
    s = urllib.urlopen(url)
    #print s.getcode()
    return s.getcode()

class Curl(threading.Thread):

    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        s = urllib.urlopen(self.url)
        print s.getcode(),self.url

