from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    hostname = models.CharField(max_length=255, verbose_name='Hostname')
    ip_address = models.CharField(max_length=255, verbose_name='Ip_address')
    type_request = models.CharField(max_length=255, verbose_name='Type')


class AlienUser(models.Model):
    username = models.CharField(max_length=255, verbose_name='username')
    hostname = models.CharField(max_length=255, verbose_name='Hostname')
    ip_address = models.CharField(max_length=255, verbose_name='Ip_address')
    type_request = models.CharField(max_length=255, verbose_name='Type')
