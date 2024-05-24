from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255)
    date = models.CharField(max_length=255)