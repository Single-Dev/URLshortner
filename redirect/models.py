from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import datetime

class CustomeUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


class URLshortner(models.Model):
    url = models.CharField(max_length=75)
    slug = models.SlugField(unique=True)
    added_date = models.DateField(default=datetime.time().now())
    def __str__(self):
        return f"id: {self.pk}"