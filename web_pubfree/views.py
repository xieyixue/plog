
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from web_models import models
from web_task.views import Scmd






def server_info(request):
    servers = models.Server.objects.values("id","ip","port","app","path")


    return  render_to_response("pubfree/server_info.html",{"servers":servers})


def server_handle(request):

    if request.method == "POST":
        id = request.POST.get("id")
        handle = request.POST.get("handle")

        #print(handle)


        server = models.Server.objects.filter(id=id).values("ip","port","path","start","stop","update","rollback")[0]

        if handle == "start":
            handle = server["start"]
        elif handle == "stop":
            handle = server["stop"]
        elif handle == "update":
            handle = "{0} {1}".format(server["update"],server["path"])


        else:
            return HttpResponse(404)
        s = Scmd(server["ip"],handle)
        s.start()

    return HttpResponse(200)

