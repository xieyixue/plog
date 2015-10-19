#!/usr/bin/env python
import urllib
def urlpost(data):
    data = urllib.urlencode(data)
    req = urllib2.Request("http://192.168.1.101",)
