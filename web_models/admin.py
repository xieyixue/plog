# -*- coding: utf-8 -*-
from django.contrib import admin
from web_models import models
# Register your models here.
admin.site.register(models.UrlCount)
admin.site.register(models.IPCount)
admin.site.register(models.WebServer)
admin.site.register(models.Server)



