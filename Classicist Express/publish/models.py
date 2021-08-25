from django.db import models


# Create your models here.
class News(models.Model):
    category = models.CharField(max_length=30)
    heading = models.CharField(max_length=200)
    news = models.CharField(max_length=1200)
    tags = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='news/', null=True)
