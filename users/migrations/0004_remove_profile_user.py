# Generated by Django 3.2.9 on 2021-12-20 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_user_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
