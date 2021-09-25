from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=60, null=True)
    date = models.CharField(max_length=30, null=True)
    comment = models.CharField(max_length=500, null=True)
