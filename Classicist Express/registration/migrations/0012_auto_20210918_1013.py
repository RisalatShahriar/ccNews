# Generated by Django 3.2.6 on 2021-09-18 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_auto_20210917_0032'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Links',
        ),
        migrations.RemoveField(
            model_name='data',
            name='state',
        ),
    ]
