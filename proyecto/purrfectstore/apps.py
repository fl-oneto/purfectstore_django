from django.apps import AppConfig



class PurrfectstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'purrfectstore'

def ready(self):
        import purrfectstore.signals  