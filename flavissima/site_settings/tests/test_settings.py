import shutil
import tempfile

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.template.loader import render_to_string
from django.templatetags.static import static
from django.test import RequestFactory, TestCase, override_settings
from django.urls import reverse
from wagtail.images import get_image_model
from wagtail.images.tests.utils import get_test_image_file
from wagtail.models import Site

from flavissima.site_settings.models import FlavissimaSiteSetting

HEADER_TEMPLATE = "flavissima/sections/header.html"
DEFAULT_LOGO = "flavissima/img/logo.svg"


class HeaderSiteSettingsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.site = Site.objects.get(is_default_site=True)

    def setUp(self):
        self.site_settings = FlavissimaSiteSetting.for_site(self.site)

    def update_settings(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self.site_settings, field, value)
        self.site_settings.save()

    def render_header(self, user=None):
        request = RequestFactory().get("/")
        request.user = user or AnonymousUser()
        return render_to_string(HEADER_TEMPLATE, request=request)

    # Title and tagline

    def test_site_title_set(self):
        self.update_settings(site_title="My Site")
        self.assertIn("My Site", self.render_header())

    def test_site_title_empty(self):
        self.update_settings(site_title="")
        self.assertNotIn("Site title", self.render_header())

    def test_site_tagline_set(self):
        self.update_settings(site_tagline="A nice tagline")
        html = self.render_header()
        self.assertIn("A nice tagline", html)
        self.assertIn("<em", html)

    def test_site_tagline_empty(self):
        self.update_settings(site_tagline="")
        self.assertNotIn("<em", self.render_header())

    # Logo

    def test_site_logo_unset_shows_flavissima_logo(self):
        self.assertIn(static(DEFAULT_LOGO), self.render_header())

    def test_site_logo_set(self):
        media_root = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, media_root)
        with override_settings(MEDIA_ROOT=media_root):
            logo = get_image_model().objects.create(
                title="Logo", file=get_test_image_file()
            )
            self.update_settings(site_title="My Site", site_logo_file=logo)
            html = self.render_header()
        self.assertIn("<img", html)
        self.assertIn('alt="My Site"', html)
        self.assertNotIn(static(DEFAULT_LOGO), html)

    # Beta tag

    def test_beta_tag_on(self):
        self.update_settings(beta_tag=True)
        self.assertIn("BETA", self.render_header())

    def test_beta_tag_off(self):
        self.update_settings(beta_tag=False)
        self.assertNotIn("BETA", self.render_header())

    # Search bar

    def test_search_bar_on(self):
        self.update_settings(search_bar=True)
        html = self.render_header()
        self.assertIn(f'action="{reverse("search")}"', html)
        self.assertIn('name="query"', html)

    def test_search_bar_off(self):
        self.update_settings(search_bar=False)
        html = self.render_header()
        self.assertNotIn(reverse("search"), html)
        self.assertNotIn('name="query"', html)

    # Login button

    def test_login_button_on_anonymous(self):
        self.update_settings(header_login_button=True)
        self.assertIn(reverse("wagtailadmin_login"), self.render_header())

    def test_login_button_on_authenticated(self):
        self.update_settings(header_login_button=True)
        user = get_user_model().objects.create_user(username="jane", password="pw")
        self.assertNotIn(reverse("wagtailadmin_login"), self.render_header(user))

    def test_login_button_off(self):
        self.update_settings(header_login_button=False)
        self.assertNotIn(reverse("wagtailadmin_login"), self.render_header())
