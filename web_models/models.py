# -*- coding: utf-8 -*-
from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.
class UrlCount(models.Model):
    url = models.CharField(max_length=500)
    count = models.IntegerField()
    date = models.CharField(max_length=500)

    def __unicode__(self):
        return "{0} {1} {2}".format(self.date,self.count,self.url)
class IPCount(models.Model):
    ip = models.CharField(max_length=500)
    count = models.IntegerField()
    date = models.CharField(max_length=500)

    def __unicode__(self):
        return "{0} {1} {2}".format(self.ip,self.count,self.date)



class PVForDay(models.Model):
    count = models.IntegerField()
    time = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

class WebServer(models.Model):
    hostname = models.CharField(max_length=200)
    port = models.IntegerField()
    url = models.URLField()
    app = models.CharField(max_length=200)

    def __unicode__(self):
        return "{0} {1} {2} {3}".format(self.hostname,self.port,self.url,self.app)

class Server(models.Model):
    ip = models.GenericIPAddressField()
    port = models.IntegerField(default=22)
    app = models.CharField(max_length=22)
    path = models.CharField(max_length=200)
    start = models.CharField(max_length=200)
    stop = models.CharField(max_length=200)
    url = models.URLField(default="127.0.0.1:8080")

    def __unicode__(self):
        return "{0} {1} {2} {3} {5}".format(self.ip,self.port,self.app,self.path,self.start,self.stop)