from django.db import models
from django.shortcuts import render_to_response

def url_count(request):
    return render_to_response("url_count_table.html")
~                                                        
