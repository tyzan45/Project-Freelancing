from django.apps import AppConfig


class StartmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'startme'

    def ready(self):
        import startme.signals

