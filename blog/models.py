from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """ Post table

    1. User object will be used as a foreign key. This is a one-to-many
       relationship, i.e., one user can have many posts. Using the 'cascade'
       option, if a user is deleted, all associated posts will also be
       deleted.

    2. Published will have the timezone based on the user's location. Note
       that now is used instead of now() because the function is being
       passed as an argument and not evaluated.
       This field will not have to be passed explicitly.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author} {self.title} {self.content}"
