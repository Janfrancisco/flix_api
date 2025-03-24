from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    # Sempre que criar um usuário, adiciona o mesmo a grupo 'customer_user'
    def ready(self):
        import authentication.signals
