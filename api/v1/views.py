from django.template.loader import render_to_string
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api import models
from api.v1 import serializers


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=True, url_path='zone-file')
    def zone_file(self, request, pk=None):
        zone = self.get_object()
        zone_file = render_to_string('zone.txt', context={'z': zone})

        resp = HttpResponse(zone_file, content_type='text/plain')
        resp['X-Zone-ID'] = zone.id
        resp['X-Zone-Domain'] = zone.domain
        resp['X-Zone-Serial'] = zone.serial
        return resp


class RecordViewSet(viewsets.ModelViewSet):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer
    permission_classes = [permissions.AllowAny]


class NameServerViewSet(viewsets.ModelViewSet):
    queryset = models.NameServer.objects.all()
    serializer_class = serializers.NameServerSerializer
    permission_classes = [permissions.AllowAny]
