from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profile.objects.create(user=self.user, home_address='123 Main St', phone_number='555-1234', location='POINT(-122.1 37.5)')

    def test_profile_page(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.profile.home_address)
        self.assertContains(response, self.profile.phone_number)
        self.assertContains(response, str(self.profile.location))

    def test_edit_profile_page(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home Address')
        self.assertContains(response, 'Phone Number')
        self.assertContains(response, 'Location')

    def test_map_page(self):
        response = self.client.get(reverse('map'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, str(self.profile.location))

# Create your tests here.
