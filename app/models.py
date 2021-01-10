'''
+ See what tables will be created in the database:
python manage.py makemigrations

+ Stage changes (this will COMMIT):
python manage.py sqlmigrate APPLICATION_NAME MIGRATION_NUMBER

+ Publish above changes:
python manage.py migrate
'''

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
