from django.db import models

# Create your models here.
class UrlCount(models.Model):
    url = models.CharField(max_length=500)
    count = models.IntegerField()
    create_at=models.DateTimeField(blank=True,auto_now_add=True)

    def __unicode__(self):
        return "{0} {1} {2}".format(self.create_at,self.count,self.url)
