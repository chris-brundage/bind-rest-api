from rest_framework import serializers
from api import models


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zone
        fields = ('id', 'domain', 'authoritative_ns', 'serial', 'filename', 'admin_email', 'default_ttl',
                  'zone_admin', 'serial_version', 'created_at', 'updated_at', 'record_set',
                  'active')
        read_only_fields = (
            'created_at', 'updated_at', 'zone_admin', 'serial_version',
            'serial')
        depth = 1


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Record
        fields = ('id', 'host', 'record_type', 'target', 'ip', 'data',
                  'mx_priority', 'mx_host', 'txt_data', 'ttl', 'created_at',
                  'updated_at', 'zone')
        read_only_fields = ('data', 'created_at', 'updated_at')


class NameServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NameServer
        fields = ('id', 'host', 'ip', 'is_authoritative', 'zone')
