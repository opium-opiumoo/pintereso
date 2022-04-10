from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from pintereso.web.models import Profile

UserModel = get_user_model()

class UserProfileViewTest(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'testuser@gmail.com',
        'password': 'Qwerty@123'
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'Testov',
        'date_of_birth': date(1990, 4, 13),
    }

    def test_when_opening_not_existing_profile__expect_404(self):
        pass

    def test_expect_correct_template(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        response = self.client.get(reverse('account'), kwargs={
            'pk': profile.pk,
        })
        self.assertTemplateUsed('author.html')

    def test_when_owner__is_owner__should_be_true(self):
        pass

    def test_when_not_owner__is_owner__should_be_false(self):
        pass

    def test_when_no_photos__no_photos_count(self):
        pass

    def test_when_photos__should_return_owners_photos(self):
        pass

    def test_when_no_photos__photos_should_be_empty(self):
        pass