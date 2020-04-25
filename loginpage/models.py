from django.db import models

# Create your models here.
class users(models.Model):
    username = models.EmailField(max_length=254,primary_key=True)
    passwords = models.CharField(max_length=32)
