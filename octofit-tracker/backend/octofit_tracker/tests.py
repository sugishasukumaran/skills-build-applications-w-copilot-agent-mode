from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout', suggested_for_team=self.team)
        self.activity = Activity.objects.create(user=self.user, activity_type='Test Activity', duration_minutes=60, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=50)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Test User')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

    def test_activity_str(self):
        self.assertIn('Test User', str(self.activity))

    def test_leaderboard_str(self):
        self.assertIn('Test Team', str(self.leaderboard))
