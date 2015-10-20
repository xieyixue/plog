from django.db import models

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