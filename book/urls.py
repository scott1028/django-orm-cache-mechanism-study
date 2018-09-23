from django.urls import path

from . import views

# Django restful-framework sample
from rest_framework import routers
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'storage', views.StorageViewSet)  # /book/api/storage/
router.register(r'storageHTML', views.StorageHTMLViewSet)  # /book/api/storage/
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]