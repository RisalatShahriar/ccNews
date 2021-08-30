from django.db import models


# Create your models here.
class News(models.Model):
    category = models.CharField(max_length=30)
    heading = models.CharField(max_length=200)
    news = models.CharField(max_length=1200)
    name = models.CharField(max_length=50)
    click = models.IntegerField(null=False)
    picture = models.ImageField(upload_to='news/', null=True)
