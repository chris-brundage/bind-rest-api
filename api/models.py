from django.db import models
import re


class Zone(models.Model):
    domain = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    admin_email = models.EmailField(max_length=255)
    default_ttl = models.IntegerField(default=3600)
    serial_version = models.IntegerField(default=0, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    refresh_ttl = models.IntegerField(default=28800)
    retry_ttl = models.IntegerField(default=1800)
    expire_ttl = models.IntegerField(default=604800)
    min_ttl = models.IntegerField(default=86400)
    active = models.BooleanField(default=False, blank=True, null=False)

    @property
    def authoritative_ns(self):
        try:
            for ns in self.nameservers:
                if ns.is_authoritative:
                    return ns.host_fqdn
        except AttributeError:
            pass

        return '.'

    @property
    def fqdn(self):
        return self.domain + '.'

    @property
    def serial(self):
        return '{:%Y%m%d}{:#02}'.format(self.updated_at, self.serial_version)

    @property
    def zone_admin(self):
        zone_admin = self.admin_email.replace('@', '.')
        if not zone_admin.endswith('.'):
            zone_admin += '.'
        return zone_admin

    def __str__(self):
        return self.domain


class Host(models.Model):
    hostname = models.CharField(max_length=255, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    @property
    def host_rel(self):
        if self.hostname == '' or self.hostname == self.zone.domain:
            return '@'

        re_match = r'\.' + re.escape(self.zone.domain) + '\.?'
        if not re.match(re_match, self.hostname, re.IGNORECASE):
            return self.hostname
        else:
            return re.sub(re_match, '', self.hostname, re.IGNORECASE)

    @property
    def host_fqdn(self):
        if self.hostname.endswith('.'):
            return self.hostname
        if self.hostname.endswith(self.zone.domain):
            return self.hostname + '.'
        return '{}.{}.'.format(self.hostname, self.zone.domain)


class Record(Host):
    record_type = models.CharField(max_length=25)
    target = models.CharField(max_length=255, default=None, blank=True,
                              null=True)
    ip = models.GenericIPAddressField(default=None, blank=True, null=True)
    mx_priority = models.IntegerField(default=None, blank=True, null=True)
    mx_host = models.CharField(max_length=255, default=None, blank=True,
                               null=True)
    txt_data = models.TextField(default=None, blank=True, null=True)
    ttl = models.IntegerField(default=3600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, blank=True, null=False)

    @property
    def data(self):
        if self.record_type == 'mx':
            data = '{} {}'.format(self.mx_priority, self.mx_host)
        elif self.record_type in ('a', 'aaaa'):
            data = '{}'.format(self.ip)
        elif self.record_type == 'cname':
            data = '{}'.format(self.target)
        elif self.record_type == 'txt':
            data = '"{}"'.format(self.txt_data.strip('"'))
        else:
            raise NotImplementedError()

        return data

    def __str__(self):
        return '{}\t\t{}\t{}'.format(self.host_rel, self.record_type.upper(),
                                     self.data)


class NameServer(Host):
    ip = models.GenericIPAddressField(unpack_ipv4=True, null=True, blank=True,
                                      default=None)
    is_authoritative = models.BooleanField(default=False, null=False,
                                           blank=True)

    def __str__(self):
        return '{} ({})'.format(self.host_fqdn.rstrip('.'), self.ip)

    class Meta:
        verbose_name_plural = 'Name Servers'
