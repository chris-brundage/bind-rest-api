from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.v1 import views


router = DefaultRouter()
router.register(r'zones', views.ZoneViewSet)
router.register(r'records', views.RecordViewSet)
router.register(r'name-servers', views.NameServerViewSet)

url_patterns = [
    url(r'^', include(router.urls)),
]
