#!/usr/bin/env python
import urllib
import urllib2
import sys
import commands
def urlpost(data,type):
    data = urllib.urlencode(data)
    req = urllib2.urlopen("http://192.168.15.109:8000/api/post_{0}/".format(type),data)
    print req.read()


def get_urlcount(logfile):
    logfile = logfile

    d = {}
    f = open(logfile,'rU')
    for line in f.readlines():
        line=line.split(" ")
        url = line[6].split(';')[0]
        try:
            d[url] = d[url] + 1
        except Exception:
            d[url] = 1
    return d

def get_ipcount(logfile):

    logfile = logfile

    d = {}
    f = open(logfile,'rU')
    for line in f.readlines():
        line=line.split(" ")
        ip = line[0]
        try:
            d[ip] = d[ip] + 1
        except Exception:
            d[ip] = 1
    return d

def get_pvforday(logfile):

    logfile = logfile
    date=logfile.split("access_")[1].split(".")[0]


    d = {}
    for i in range(00,24):
        i = str(i)
        if len(i) == 1:
            i = "0" + i
        print i
        count=commands.getoutput("grep -c 2015\:{0} {1}".format(i,file))
        print count
        d[i] = count

    datas = {"data":d,"day":date}

    return datas


if __name__ == "__main__":

    logfile = sys.argv[1]
    date=logfile.split("access_")[1].split(".")[0]

    urlcounts = get_urlcount(logfile)
    ipcounts = get_ipcount(logfile)

    ipdata={"data":ipcounts,"date":date}
    urldata={"data":urlcounts,"date":date}

    pvfordaydate=get_pvforday()

    #urlpost(ipdata,"ipcount")
    #urlpost(urldata,"urlcount")
    urlpost(pvfordaydate,"pvforday")