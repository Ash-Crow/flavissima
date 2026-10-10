from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from flavissima.blocks import STREAMFIELD_COMMON_BLOCKS


class ContentPage(Page):
    hero = StreamField(
        STREAMFIELD_COMMON_BLOCKS,
        blank=True,
    )
    body = StreamField(
        STREAMFIELD_COMMON_BLOCKS,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero"),
        FieldPanel("body"),
    ]
