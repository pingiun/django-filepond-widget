import json
from django import forms
from django.core.files.base import File

from django_drf_filepond.models import TemporaryUpload


class FilePondWidget(forms.FileInput):
    needs_multipart_form = True
    template_name = "filepond_widget/widget.html"

    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.filepond_options = {}

    def value_from_datadict(self, data, files, name):
        upload_id = data.get(name)
        if upload_id is None:
            return files.get(name)
        return upload_id

    def value_omitted_from_data(self, data, files, name):
        return name not in data and name not in files

    def get_context(self, name: str, value, attrs):
        context = super().get_context(name, value, attrs)
        context["filepond_options"] = json.dumps(self.filepond_options)
        return context


class FilePondField(forms.FileField):
    widget = FilePondWidget

    def __init__(
        self,
        *,
        max_length=None,
        allow_empty_file=False,
        filepond_options=None,
        **kwargs
    ):
        super().__init__(
            max_length=max_length, allow_empty_file=allow_empty_file, **kwargs
        )
        self.widget.filepond_options = filepond_options or {}

    def to_python(self, data):
        if isinstance(data, str):
            temp_upload = TemporaryUpload.objects.get(upload_id=data)
            return File(temp_upload.file, name=temp_upload.upload_name)
        return super().to_python(data)
