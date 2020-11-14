from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

"""
Authentication
many   to  one   to    one
R R R <-- Author <--> Django User

"""
# Create your models here.
"""
author model
- id
- name
- email

recipes model
- id
- title
- body
- author (FK)Foreign Key
- time

"""


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Recipes(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
