from django.shortcuts import HttpResponse
import json
from web_models import models
# Create your views here.
def get_urlcount(request):
    print "------------"
    if request.method == "GET":
        data = models.UrlCount.objects.values("url","count")
        print data
        d = []
        for i in data:
            d.append(i)
        d = json.dumps(d)
        return HttpResponse(d)

