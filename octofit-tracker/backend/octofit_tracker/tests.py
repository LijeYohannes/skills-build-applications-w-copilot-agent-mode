from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, User, Activity, Workout, Leaderboard

class OctofitTrackerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.marvel = Team.objects.create(name='Marvel')
        self.dc = Team.objects.create(name='DC')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.marvel)
        self.workout = Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Hard')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, calories=300, date='2025-12-04')
        self.leaderboard = Leaderboard.objects.create(team=self.marvel, points=700)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)

    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_activities_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workouts_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
