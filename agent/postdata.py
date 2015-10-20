#!/usr/bin/env python
import urllib
import urllib2
def urlpost(data):
    data = urllib.urlencode(data)
    req = urllib2.urlopen("http://192.168.15.109:8000/api/post_urlcount/",data)
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


if __name__ == "__main__":
    logfile = "access_2015-10-16.log"
    date = "2015-10-16"

    #d = get_urlcount(logfile)
    d = get_ipcount(logfile)
    data={"data":d,"date":date}
    urlpost(data)