from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.images import get_image_model_string

# Create your models here.


@register_setting(icon="cog")
class FlavissimaSiteSetting(ClusterableModel, BaseSiteSetting):
    class Meta:
        verbose_name = _("Site configuration")
        verbose_name_plural = _("Site configurations")

    site_title = models.CharField(
        _("Site title"),
        max_length=200,
        default=_("Site title"),  # type: ignore
        blank=True,
    )
    site_tagline = models.CharField(
        _("Site tagline"),
        max_length=200,
        default=_("Site tagline"),  # type: ignore
        blank=True,
    )

    # Site logo
    site_logo_file = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Site logo"),
    )

    beta_tag = models.BooleanField(
        _("Show the BETA tag next to the title"), default=False
    )

    header_login_button = models.BooleanField(
        _("Show a login button in the header"), default=False
    )

    search_bar = models.BooleanField(_("Display search bar in the header"), default=False)  # type: ignore

    site_panels = [
        FieldPanel("site_title"),
        FieldPanel("site_tagline"),
        MultiFieldPanel(
            [
                FieldPanel("site_logo_file"),
            ],
            heading=_("Site logo"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("beta_tag"),
                FieldPanel("header_login_button"),
                FieldPanel("search_bar"),
            ],
            heading=_("Advanced settings"),
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(site_panels, heading=_("Generic")),
        ]
    )
