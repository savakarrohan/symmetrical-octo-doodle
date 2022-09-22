from django.test import SimpleTestCase
from django.urls import reverse,resolve

from pages.views import HomePageView
# Classes for the Homepage with layout home.html
class HomepageTests(SimpleTestCase):
    """ tests for the Homepage"""
    def setUp(self):
        """Set up of self for tests"""
        url = reverse("home")
        self.response = self.client.get(url)
    def test_url_exists_at_correct_location(self):
        """url location"""
        self.assertEqual(self.response.status_code,200)
    def test_homepage_url_name(self):
        """ url name"""
        self.assertEqual(self.response.status_code,200)
    def test_homepage_template(self):
        """ template"""
        self.assertTemplateUsed(self.response, "home.html")
    def test_homepage_contains_correct_html(self):
        """ text at link"""
        self.assertContains(self.response, "home page")
    def test_homepage_does_not_contain_incorrect_html(self):
        """ test for not required text"""
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
    def test_homepage_url_resolves_homepageview(self):
        """ check if the names are corect at both links"""
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)