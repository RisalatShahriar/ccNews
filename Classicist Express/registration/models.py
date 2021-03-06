from django.db import models


# Create your models here.
class Data(models.Model):
    accessID = models.CharField(max_length=64)
    email = models.EmailField(max_length=90)
    number = models.IntegerField()
    image = models.ImageField(null=True, upload_to='profile_pictures/')
    address = models.CharField(max_length=128)
    post = models.CharField(max_length=20)
