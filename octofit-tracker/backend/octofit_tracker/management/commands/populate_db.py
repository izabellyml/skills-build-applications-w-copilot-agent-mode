from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Add test data for users
        User.objects.create(email='john.doe@example.com', name='John Doe', password='password123')
        User.objects.create(email='jane.smith@example.com', name='Jane Smith', password='password456')

        # Add test data for teams
        Team.objects.create(name='Team Alpha', members=['john.doe@example.com', 'jane.smith@example.com'])

        # Add test data for activities
        Activity.objects.create(user=User.objects.get(email='john.doe@example.com'), activity_type='Running', duration=30)
        Activity.objects.create(user=User.objects.get(email='jane.smith@example.com'), activity_type='Cycling', duration=45)

        # Add test data for leaderboard
        Leaderboard.objects.create(user=User.objects.get(email='john.doe@example.com'), score=100)
        Leaderboard.objects.create(user=User.objects.get(email='jane.smith@example.com'), score=150)

        # Add test data for workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session to start the day.')
        Workout.objects.create(name='HIIT', description='High-intensity interval training for advanced users.')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
