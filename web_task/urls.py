from django.conf.urls import  url
from web_task import views
urlpatterns = [
    url("^server_info",views.server_info),
    url("^test",views.cmd_run),

]

