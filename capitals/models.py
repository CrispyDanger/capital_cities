from django.db import models
from django.urls import reverse


class City(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}"

    def get_absolute_url(self):
        return reverse("home")


# Create your models here.
