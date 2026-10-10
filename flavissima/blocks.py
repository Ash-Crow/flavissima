from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.images.blocks import ImageBlock

from flavissima.constants import RICHTEXTFIELD_FEATURES

## Streamblocks definitions
STREAMFIELD_COMMON_BLOCKS = [
    (
        "section",
        blocks.RichTextBlock(features=RICHTEXTFIELD_FEATURES, label=_("Paragraph")),
    ),
    ("image", ImageBlock(label=_("Image"))),
    (
        "html",
        blocks.RawHTMLBlock(
            readonly=True,
            help_text=_(
                "Warning: Use HTML block with caution. Malicious code can compromise the security of the site."
            ),
            group=_("5. Expert syntax"),
        ),
    ),
]
