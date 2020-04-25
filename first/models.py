from django.db import models

# Create your models here.
class branch(models.Model):
    b_name= models.CharField(max_length=100)
    b_img = models.ImageField(upload_to='pics')
    b_desc= models.TextField()
