from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import LoginForm
from users.views import *

# Create your tests here.

class UrlTestCase(SimpleTestCase):

    def test_login_url_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_user_home_url_resolved(self):
        url = reverse('user_home')
        self.assertEquals(resolve(url).func, user_home_view)

