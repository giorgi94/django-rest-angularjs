from django import forms
from django.core import exceptions
from django.db import models
import json
from .mediaPIL import MediaPIL
from .widgets import ImagePILWidget


class ImagePILField(models.TextField):
    description = "Image PIL Field"

    def __init__(self, pathway=None, point=(50, 50), quality=90,
                 upload_to=".", *args, **kwargs):
        self.pathway = pathway
        self.point = point
        self.quality = quality
        self.upload_to = upload_to
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        try:
            if value is None:
                return MediaPIL()
            kwargs = json.loads(value)
            return MediaPIL(**kwargs)
        except:
            return MediaPIL()

    def get_prep_value(self, value):
        return value.to_str()

    def formfield(self, **kwargs):
        kwargs['widget'] = ImagePILWidget
        return super().formfield(**kwargs)


"""
from apps.blog.models import Blog
blog = Blog.objects.all()[0]
blog.image
"""
