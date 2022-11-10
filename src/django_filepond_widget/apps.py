from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FilepondWidgetConfig(AppConfig):
    """AppConfig class for Filepond Widget app."""

    name = "django_filepond_widget"
    verbose_name = _("Filepond Widget")
