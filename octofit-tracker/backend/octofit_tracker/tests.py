from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, User, Activity, Workout, Leaderboard

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.dc = Team.objects.create(name='DC', description='DC Superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.marvel, is_superhero=True)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('teams', response.data)

    def test_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list) or 'results' in response.data)

    def test_teams_endpoint(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list) or 'results' in response.data)
