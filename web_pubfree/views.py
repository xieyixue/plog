from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from web_models import models
import threading
import paramiko


class Scmd(threading.Thread):

    def __init__(self,ip,cmd,port=22,user="root",pkey="/root/.ssh/id_rsa",password="000000"):
        threading.Thread.__init__(self)
        self.ip       = ip
        self.password = password
        self.cmd      = cmd
        self.port     = port
        self.user     = user
        self.pkey     = paramiko.RSAKey.from_private_key_file(pkey)
        self.PROFILE  = ". /etc/profile 2&>/dev/null;. ~/.bash_profile 2&>/dev/null;. /etc/bashrc 2&>/dev/null;. ~/.bashrc 2&>/dev/null;"
        self.PATH     = "export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin;"
        self.result   = ""

    def run(self):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=self.ip,port=self.port,username=self.user,pkey=self.pkey)
        stdin,stdout,stderr = s.exec_command(self.PROFILE+self.PATH+self.cmd)

        output =  stdout.readlines()
        err    =  stderr.readlines()
        result = ""
        if output:
            for o in output:
                result += o
        elif err:
            for e in err:
                result += e
        else:
            result = ""
        self.result = result
        #print result + '============='
        s.close()
        return  result


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

