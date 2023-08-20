from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=255, unique=True)
    time_updated = models.DateTimeField(auto_now=True)
    translation = models.CharField(max_length=255)
    context = models.TextField()

    def get_absolute_url(self):
        return reverse('words:update', args=(self.pk,))

    def __str__(self):
        return self.word