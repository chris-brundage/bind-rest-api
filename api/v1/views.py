from rest_framework import viewsets, permissions
from api import models
from api.v1 import serializers


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer
    permission_classes = [permissions.AllowAny]


class RecordViewSet(viewsets.ModelViewSet):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer
    permission_classes = [permissions.AllowAny]


class NameServerViewSet(viewsets.ModelViewSet):
    queryset = models.NameServer.objects.all()
    serializer_class = serializers.NameServerSerializer
    permission_classes = [permissions.AllowAny]
