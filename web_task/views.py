#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from web_models import models
import threading
import paramiko

def server_info(request):

    servers = models.Server.objects.values("id","ip","port")

    return render_to_response("task/server_info.html",{"servers":servers})

