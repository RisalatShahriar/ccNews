# Generated by Django 3.2.6 on 2021-08-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0004_news_click'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='click',
            field=models.IntegerField(),
        ),
    ]