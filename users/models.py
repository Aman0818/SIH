from django.db import models
from django.contrib.auth.models import AbstractUser
from trees.models import Tree

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    coordinates = models.CharField(max_length=255, blank=True, null=True)
    bookmarks = models.ManyToManyField(Tree, related_name='bookmarked_by', blank=True) 

    def __str__(self):
        return self.username
