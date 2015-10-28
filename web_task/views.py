#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from web_models import models
import threading
import paramiko
import Queue


class Scmd(threading.Thread):

    def __init__(self,
                 ip,
                 cmd,
                 resultQ,
                 port=22,
                 user="root",
                 pkey="/root/.ssh/id_rsa",
                 password="000000"):

        threading.Thread.__init__(self)
        self.ip       = ip
        self.password = password
        self.cmd      = cmd
        self.port     = port
        self.user     = user
        self.pkey     = paramiko.RSAKey.from_private_key_file(pkey)
        self.PROFILE  = ". /etc/profile 2&>/dev/null;. ~/.bash_profile 2&>/dev/null;. /etc/bashrc 2&>/dev/null;. ~/.bashrc 2&>/dev/null;"
        self.PATH     = "export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin;"
        self.result   = resultQ

    def run(self):
       #print "--------"
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=self.ip,port=self.port,username=self.user,pkey=self.pkey)
        stdin,stdout,stderr = s.exec_command(self.PROFILE+self.PATH+self.cmd)

        output =  stdout.readlines()
        err    =  stderr.readlines()
        result = str(self.ip + "\n")
        if output:
            for o in output:
                result += o
        elif err:
            for e in err:
                result += e
        else:
            result = ""
        self.result.put(result)
        #print result,"--------"
        s.close()
        return  result



def server_info(request):

    servers = models.Server.objects.values("id","ip","port")

    return render_to_response("task/server_info.html",{"servers":servers})

def cmd_run(request):
    if request.method == "GET":
        # ids = request.POST.get("ids","")
        # cmd = request.POST.get("cmd","")
        cmd = "df"
        ids = ["192.168.111.11","192.168.111.12","192.168.111.13","192.168.111.14","192.168.111.12"]
        resultQ = Queue.Queue(maxsize=0)
        for i in ids:
            i = Scmd(i,cmd,resultQ)
            i.start()
        count = 0
        result = ""
        while count < len(ids):

             if resultQ.empty():
                 pass
             else:
                 result += resultQ.get()
                 count += 1

    return HttpResponse(result)




