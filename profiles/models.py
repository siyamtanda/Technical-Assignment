from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models

class CustomUser(AbstractUser):
    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    location = models.PointField(null=True)

# Create your models here.
