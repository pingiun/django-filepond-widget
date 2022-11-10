from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FilepondWidgetConfig(AppConfig):
    """AppConfig class for Filepond Widget app."""

    name = "filepond_widget"
    verbose_name = _("Filepond Wisdget")
