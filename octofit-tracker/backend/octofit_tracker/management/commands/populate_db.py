from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Hard'),
            Workout.objects.create(name='Strength Builder', description='Weight training', difficulty='Medium'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date=date.today())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400, date=date.today())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=500, date=date.today())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, calories=200, date=date.today())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=700)
        Leaderboard.objects.create(team=dc, points=600)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
