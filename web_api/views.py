from django.shortcuts import HttpResponse
import json
from web_models import models
# Create your views here.
def get_urlcount(request,day):
    ##print "------------"
    if request.method == "GET":
        data = models.UrlCount.objects.filter(date=day).values("url","count","date")
        #print data
        d = []
        for i in data:
            d.append(i)
        d = json.dumps(d)
        return HttpResponse(d)
def get_ipcount(request,day):
    ##print "------------"
    if request.method == "GET":
        data = models.IPCount.objects.filter(date=day).values("ip","count","date")
        #print data
        d = []
        for i in data:
            d.append(i)
        d = json.dumps(d)
        return HttpResponse(d)
def post_urlcount(request):

    if request.method == "POST":
        data = request.POST.get("data","")
        date = request.POST.get("date","")
        data = eval(data)
        #print data,date
        for url in data:
            count = data[url]
            models.UrlCount.objects.create(url=url,count=count,date=date)
        return HttpResponse(200)
def post_ipcount(request):
    if request.method == "POST":
        data = request.POST.get("data","")
        date = request.POST.get("date","")
        data = eval(data)
        for ip in data:
            count = data[ip]
            models.IPCount.objects.create(ip=ip,count=count,date=date)
        return HttpResponse(200)

def post_pvforday(request):

    if request.method == "POST":
        data = request.POST.get("data","")
        day = request.POST.get("day","")

        data = eval(data)

        for  time in data:

            models.PVForDay.objects.create(date=day,time=time,count=data[time])
    return HttpResponse(200)
