# Generated by Django 3.2.6 on 2021-08-23 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20210823_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]