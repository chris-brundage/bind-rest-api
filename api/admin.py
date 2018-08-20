from django.contrib import admin
from api.models import NameServer, Record, Zone

admin.site.register(NameServer)
admin.site.register(Record)
admin.site.register(Zone)

