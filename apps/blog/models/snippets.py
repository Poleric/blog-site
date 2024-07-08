from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=100)
    author_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel("name"),
        FieldPanel('author_image')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Authors"
