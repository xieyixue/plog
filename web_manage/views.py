#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from web_models import models

# Create your views here.

def insent_log(request):
    d = {}
    logfile = "log/nginx/access_2015-10-17.log"
    date = "2015-10-17"
    f = open(logfile,'rU')
    for line in f.readlines():
        line=line.split(" ")
        url = line[6].split(';')[0]
        try:
            d[url] = d[url] + 1
        except Exception:
            d[url] = 1

    for url in d:
        count = d[url]
        models.UrlCount.objects.create(url=url,count=count,date=date)
def  get_urlcount(request,*args):
    if args != "":

        data = args[0]
        return render_to_response("url_count_table.html",{"day":data})
    else:
        return render_to_response("url_count_table.html",{"day":"2015-10-16"})
def  get_ipcount(request,*args):
    if args != "":

        data = args[0]
        return render_to_response("ip_count_table.html",{"day":data})
    else:
        return render_to_response("ip_count_table.html",{"day":"2015-10-16"})
def base(request):
    datas = models.UrlCount.objects.filter(url="/").values("date")

    d = []
    for data in datas:
        d.append(data["date"])
    #datas=["2015-10-16","2015-10-17","2015-10-18","2015-10-19","2015-10-20",]
    return render_to_response("base.html",{"datas":d})

def char(request,day):

    data = models.PVForDay.objects.filter(date=day).values("time","count")

    data_ = sorted(data,key=lambda  s: s["time"])
    '''
    _list = []
    for i in range(00,24):
        i = str(i)
        if len(i) == 1:
            i = "0" + i
        print i

        for times in data:
            print times
            if times["time"] == i:

                _list.append(times)
    print list
    '''

    return render_to_response("char.html",{"data":data_,"date":day})