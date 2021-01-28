from django.test import SimpleTestCase
from users.forms import SignUpForm


class TestForms(SimpleTestCase):

    def test_signupform_valid_data(self):
        form = SignUpForm(data={
            'username': 'john_doe',
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'testpassword1234'
        })

        self.assertTrue(form.is_valid())


    def test_signupform_no_data(self):
        form = SignUpForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)