# Generated by Django 3.2.6 on 2021-08-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_data_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
