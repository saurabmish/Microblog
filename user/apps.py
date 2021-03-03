from django.apps import AppConfig

class UsersConfig(AppConfig):
    """The name attribute has to match the directory name."""
    name = 'user'

    def ready(self):
        import user.signals
