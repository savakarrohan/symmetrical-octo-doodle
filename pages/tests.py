from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse
# Classes for the Homepage with layout home.html
class HomepageTests(SimpleTestCase):
    """ tests for the Homepage"""
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
    def test_homepage_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        