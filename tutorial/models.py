from django.db import models

# Create your models here.
class hackerrank(models.Model):
    name=models.CharField(max_length=100)
    problem=models.TextField()
    solution=models.TextField()
    video=models.CharField(max_length=100)