# Generated by Django 4.2.2 on 2023-08-19 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
