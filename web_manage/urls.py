"""plog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

from web_manage import views
from web_manage.monitor import views as monitor

urlpatterns = [


    url(r'^char/(.+)/$',views.char),
    url(r'^get_urlcount/(.+)/$',views.get_urlcount),
    url(r'^get_ipcount/(.+)/$',views.get_ipcount),
    url(r'^base/',views.base),
    url(r'^monitor_web',monitor.monitor_web)
]
