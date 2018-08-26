import datetime
import os
import re
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from api import models
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(pre_save, sender=models.Zone)
def increment_serial(sender, instance, raw, using, update_fields, **kwargs):
    if update_fields is None or 'serial_version' not in update_fields:
        try:
            if instance.updated_at.date() == datetime.date.today():
                instance.serial_version += 1
            else:
                instance.serial_version = 0
        except (AttributeError, TypeError):
            instance.serial_version = 0


@receiver(post_save, sender=models.Record)
def update_zone(sender, instance=None, created=False, **kwargs):
    zone = instance.zone
    if zone.active:
        if zone.updated_at.date() < datetime.date.today():
            zone.serial_version = 0
            zone.save()
        else:
            zone.serial_version += 1
            zone.save(update_fields=['serial_version'])


@receiver(post_save, sender=models.Zone)
def create_zone_file(sender, instance=None, created=False, **kwargs):
    if instance.active:
        zone_file = render_to_string('zone.txt', {'z': instance})
        with open(instance.filename, 'w') as f:
            f.write(zone_file)
    else:
        try:
            os.unlink(instance.filename)
        except IOError:
            pass
