# Generated by Django 3.2.6 on 2021-08-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='password',
        ),
        migrations.AlterField(
            model_name='data',
            name='number',
            field=models.IntegerField(),
        ),
    ]
