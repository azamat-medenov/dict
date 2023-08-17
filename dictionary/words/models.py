from django.db import models

# Create your models here.
class Entry(models.Model):
    word = models.CharField(max_length=255, unique=True)
    translation = models.CharField(max_length=255)
    context = models.TextField()