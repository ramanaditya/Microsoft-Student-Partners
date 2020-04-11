from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "microsoft_student_partners.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import microsoft_student_partners.users.signals  # noqa F401
        except ImportError:
            pass
