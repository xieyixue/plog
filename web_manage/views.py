from django.shortcuts import render
from django.shortcuts import render_to_response
from web_models import models

# Create your views here.

def insent_log(request):
    d = {}
    logfile = "/app/logview/logs/nginx/access_2015-10-16.log"
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
        models.UrlCount.objects.create(url=url,count=count)
def  get_urlcount(request):
    return render_to_response("url_count_table.html")
