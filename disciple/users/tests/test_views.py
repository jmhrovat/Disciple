from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class TestAuthenticatedViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.user_home_url = reverse('user_home')


        user = User.objects.create_user('john_doe', 'myemail@test.com', 'bar')
        self.client.login(username='john_doe', password='bar')

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 302)

    def test_user_home(self):
        response = self.client.get(self.user_home_url)
        self.assertEquals(response.status_code, 200)

class TestAnonynmousViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.user_home_url = reverse('user_home')

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)

    def test_user_home(self):
        response = self.client.get(self.user_home_url)
        self.assertEquals(response.status_code, 302)



