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
        print args[0]
        data = args[0]
        return render_to_response("url_count_table.html",{"day":data})
    else:
        return render_to_response("url_count_table.html",{"day":"2015-10-16"})
def  get_ipcount(request,*args):
    if args != "":
        print args[0]
        data = args[0]
        return render_to_response("ip_count_table.html",{"day":data})
    else:
        return render_to_response("ip_count_table.html",{"day":"2015-10-16"})
def base(request):

    datas=["2015-10-16","2015-10-17","2015-10-18","2015-10-19","2015-10-20",]
    return render_to_response("base.html",{"datas":datas})

def char(request):
    data = []
    a = {"time":"01","count":12333}
    b = {"time":"02","count":5764}
    data.append(a)
    data.append(b)
    #data = {"i":1}
    return render_to_response("char.html",{"data":data})