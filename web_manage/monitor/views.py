#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from web_models import models

# Create your views here.

def monitor_web(request):

    return render_to_response("monitor/monitor_web.html")