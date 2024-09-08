from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, blank=True, verbose_name='Usuario')
    first_name = models.CharField(max_length=20, verbose_name='Nombre', blank=True)
    last_name = models.CharField(max_length=20, verbose_name='Apellido', blank=True)