import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Storage 


# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    qs = Storage.objects.all()
    data = serializers.serialize("json", qs)
    logger.info(qs)
    return HttpResponse(data, content_type='application/json')
