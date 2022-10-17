from django.contrib.auth.models import AbstractUser
from django.db import models
from audioop import add

class CustomeUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


class URLshortner(models.Model):
    url = models.CharField(max_length=75)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now=add)
    def __str__(self):
        return f"id: {self.pk}"