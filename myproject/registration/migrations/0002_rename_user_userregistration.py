# Generated by Django 3.2.25 on 2024-09-10 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserRegistration',
        ),
    ]
