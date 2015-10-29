from django.conf.urls import  url
from web_task import views
urlpatterns = [
    url("^server_info",views.server_info),
    url("^cmd_run",views.cmd_run),

]

