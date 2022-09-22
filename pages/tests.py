from django.test import SimpleTestCase
from django.urls import reverse
# Classes for the Homepage with layout home.html
class HomepageTests(SimpleTestCase):
    """ tests for the Homepage"""
    def test_url_exists_at_correct_location(self):
        """url location"""
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
    def test_homepage_url_name(self):
        """ url name"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
    def test_homepage_template(self):
        """ template"""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")
    def test_homepage_contains_correct_html(self):
        """ text at link"""
        response = self.client.get("/")
        self.assertContains(response, "home page")
    def test_homepage_does_not_contain_incorrect_html(self):
        """ test for not required text"""
        response = self.client.get("/")
        self.assertNotContains(response, "Hi there! I should not be on the page.")
    