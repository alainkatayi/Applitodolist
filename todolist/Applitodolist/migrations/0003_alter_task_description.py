# Generated by Django 5.0.7 on 2025-01-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applitodolist', '0002_task_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=20),
        ),
    ]
