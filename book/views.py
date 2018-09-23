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


# Django restful-framework sample
# from django.contrib.auth.models import User, Group
from rest_framework import serializers as restfulSerializers

class StorageSerializer(restfulSerializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storage
        fields = ('id', 'label', 'description')

# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class StorageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Storage.objects.all().order_by('-label')
    serializer_class = StorageSerializer

class StorageHTMLViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    renderer_classes = (BrowsableAPIRenderer,)  # override REST_FRAMEWORK of global settings.py

    queryset = Storage.objects.all().order_by('-label')
    serializer_class = StorageSerializer
