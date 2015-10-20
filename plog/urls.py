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
from django.contrib import admin
from web_manage import views
from web_api.views import post_urlcount,post_ipcount
from web_api.views import get_urlcount,get_ipcount
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^insent_log/',views.insent_log),

    url(r'^$',views.base),
    url(r'^char',views.char),

    url(r'^manage/get_urlcount/(.+)/$',views.get_urlcount),
    #url(r'^manage/get_urlcount/$',views.get_urlcount),

    url(r'^manage/get_ipcount/(.+)/$',views.get_ipcount),
    #url(r'^manage/get_ipcount/$',views.get_urlcount),
    url(r'^manage/base/',views.base),

    url(r'^api/get_urlcount/(.+)/$',get_urlcount),
    url(r'^api/get_ipcount/(.+)/$',get_ipcount),
    url(r'^api/post_urlcount/',post_urlcount),
    url(r'^api/post_ipcount/',post_ipcount),
]
