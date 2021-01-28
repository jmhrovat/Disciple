from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.test_user = User.objects.create(
            first_name = "John",
            last_name = "Doe",
            username = "john_doe!",
            password = "testpassword1234",
            email = "jdoe@email.com"
        )
        self.test_user.save()


    def test_profile_created_on_user_save(self):
        try:
            test_profile = Profile.objects.get(user=self.test_user)
        finally:
            self.assertEquals(test_profile.__str__(), "Doe, John")
