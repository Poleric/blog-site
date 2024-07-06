from django import forms
from django.db import models

from modelcluster.fields import ParentalManyToManyField
from wagtail.blocks import StreamBlock
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel


class HomePage(Page):
    intro = models.TextField(help_text="Text to describe the page", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    body = StreamField(
        StreamBlock(),
        verbose_name="Home content block",
        blank=True,
        use_json_field=True,
    )
    socials = ParentalManyToManyField("core.Social", blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("image"),
            FieldPanel("intro")
        ], heading="Home introduction"),
        FieldPanel("body"),
        FieldPanel("socials", widget=forms.CheckboxSelectMultiple),
    ]
