from django.apps import AppConfig


class LibraryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LibraryApp'

    def ready(self):
        '''
        Use ready hook to run code on deploy
        '''
        return
        