# Generated by Django 3.2.6 on 2021-08-23 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_alter_data_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='image',
            field=models.ImageField(null=True, upload_to='propics/'),
        ),
    ]