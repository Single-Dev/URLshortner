from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

class CustomeUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


class UrlShortner(models.Model):
    url = models.URLField(max_length=75)
    slug = models.SlugField(unique=True)
    created_on = models.DateTimeField(("created on"), default=timezone.now)
    
    def __str__(self):
        return f"id: {self.pk}"