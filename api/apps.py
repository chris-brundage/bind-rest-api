from django.apps import AppConfig


class BindApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from api import signals