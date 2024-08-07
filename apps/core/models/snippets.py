from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, TranslatableMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class FooterContent(TranslatableMixin, ClusterableModel):
    copyright_text = RichTextField()

    panels = [
        FieldPanel("copyright_text"),
        InlinePanel("footer_items"),
    ]

    def __str__(self):
        return "Footer content"


class FooterItem(TranslatableMixin, Orderable):
    parent_footer = ParentalKey(
        "core.FooterContent", on_delete=models.CASCADE, related_name="footer_items"
    )

    class IconChoice(models.TextChoices):
        INFO = "info", "Info"
        HELP = "help", "Help"
        WAGTAIL = "wagtail", "Wagtail"

    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()
    icon = models.CharField(
        max_length=7, choices=IconChoice.choices, default=IconChoice.INFO
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("link"),
        FieldPanel("icon"),
    ]

    def __str__(self):
        return self.title


@register_snippet
class Social(models.Model):
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)

    panels = [
        FieldPanel("icon"),
        FieldPanel("name"),
        FieldPanel("url")
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Socials"
