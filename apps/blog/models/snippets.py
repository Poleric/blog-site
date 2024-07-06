from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=100)

    panels = [
        FieldPanel("name")
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Authors"
