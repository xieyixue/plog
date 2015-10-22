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


class Url(models.Model):
    url = models.CharField(max_length=500)

class Date(models.Model):
    date = models.CharField(max_length=20)

class XUrlCount(models.Model):

    url = models.ForeignKey(Url)
    date = models.ForeignKey(Date)
    count = models.IntegerField()

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