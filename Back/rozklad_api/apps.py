from django.apps import AppConfig


class RozkladApiConfig(AppConfig):
    name = 'rozklad_api'

    def ready(self):
        from .scheduler import RozkladScheduler
        RozkladScheduler.start_rozklad_sync()
