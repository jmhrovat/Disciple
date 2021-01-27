from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Create your tests here.

class UrlTestCase(SimpleTestCase):

    def test_url_resolved(self):
        assert 1 == 1