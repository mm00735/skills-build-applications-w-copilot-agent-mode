from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete all data using .all().delete() in correct order
        for obj in Activity.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Workout.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Leaderboard.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for user in User.objects.all():
            if getattr(user, 'id', None):
                user.delete()
        for obj in Team.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()

        # Create teams
        marvel = Team.objects.create(id=ObjectId(), name='Team Marvel')
        dc = Team.objects.create(id=ObjectId(), name='Team DC')

        # Create users
        ironman = User.objects.create_user(id=ObjectId(), username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(id=ObjectId(), username='captainamerica', email='captain@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(id=ObjectId(), username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(id=ObjectId(), username='superman', email='superman@dc.com', password='password', team=dc)

        # Create activities
        Activity.objects.create(id=ObjectId(), user=ironman, type='run', duration=30, distance=5)
        Activity.objects.create(id=ObjectId(), user=batman, type='cycle', duration=60, distance=20)

        # Create workouts
        Workout.objects.create(id=ObjectId(), user=ironman, name='Chest Day', description='Bench press and pushups')
        Workout.objects.create(id=ObjectId(), user=batman, name='Leg Day', description='Squats and lunges')

        # Create leaderboard
        Leaderboard.objects.create(id=ObjectId(), user=ironman, points=100)
        Leaderboard.objects.create(id=ObjectId(), user=batman, points=90)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
