from django.contrib.auth.models import User
from django.db import models

class Synonym(models.Model):
    word = models.CharField(max_length=50)
    anger = models.CharField(max_length=10)
    disgust = models.CharField(max_length=10)
    fear = models.CharField(max_length=10)
    happiness = models.CharField(max_length=10)
    sadness = models.CharField(max_length=10)
    surprise = models.CharField(max_length=10)

