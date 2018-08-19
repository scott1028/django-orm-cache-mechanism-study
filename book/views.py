import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.db import connection

from .models import Storage 


# Get an instance of a logger, see the settings.py
# logger = logging.getLogger(__name__)
logger = logging.getLogger('my-custom-logger')

# Create your views here.
def index(request):
    qs = Storage.objects.all()
    data = serializers.serialize("json", qs)
    logger.debug(['=>', qs])

    # https://stackoverflow.com/questions/971667/django-orm-how-to-view-or-log-the-executed-query
    logger.debug(['=>', connection.queries])
    
    return HttpResponse(data, content_type='application/json')
