# Generated by Django 3.2.9 on 2021-12-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.AlterField(
            model_name='project',
            name='excel_file',
            field=models.FileField(upload_to='excels'),
        ),
    ]
