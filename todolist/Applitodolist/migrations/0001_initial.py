# Generated by Django 5.0.7 on 2024-12-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=8, unique=True)),
            ],
        ),
    ]
