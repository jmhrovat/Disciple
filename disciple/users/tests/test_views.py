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


        self.user = User.objects.create_user(
            first_name = "John",
            last_name = "Doe",
            username = "john_doe!",
            email = "jdoe@email.com"
        )
        self.user.set_password("testpassword1234")
        self.user.save()

        self.client.login(username='john_doe!', password='testpassword1234')


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

        self.user = User.objects.create_user(
            first_name = "John",
            last_name = "Doe",
            username = "john_doe!",
            email = "jdoe@email.com"
        )
        self.user.set_password("testpassword1234")
        self.user.save()

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

    def test_register_new_user_POST(self):
        response = self.client.post(self.register_url, {
            'username': 'test_user1234',
            'first_name': 'test',
            'last_name': 'test',
            'password': 'testpassword1234'
        })
        self.assertEquals(response.status_code, 302)

    def test_register_existing_user_POST(self):
        response = self.client.post(self.register_url, {
            'username': 'john_doe!',
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'testpassword1234'
        })

        user = authenticate(username='john_doe!', password='testpassword1234' )
        self.assertRedirects(response, '/app/', status_code=302)

    def test_user_home(self):
        response = self.client.get(self.user_home_url)
        self.assertEquals(response.status_code, 302)



