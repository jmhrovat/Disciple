from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class TestAuthenticatedViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')


        self.user = User.objects.create_user(
            first_name = "John",
            last_name = "Doe",
            username = "john_doe!",
            email = "jdoe@email.com"
        )
        self.user.set_password("testpassword1234")
        self.user.save()

        self.client.login(username='john_doe!', password='testpassword1234')

    def test_homepage(self):
        response = self.client.get(self.homepage_url)
        self.assertEquals(response.status_code, 302)

class TestAnonynmousViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')

    def test_homepage(self):
        response = self.client.get(self.homepage_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/index.html')

