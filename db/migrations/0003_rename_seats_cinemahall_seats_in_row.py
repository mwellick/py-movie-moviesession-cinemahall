# Generated by Django 4.0.2 on 2024-04-15 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_cinemahall_movie_moviesession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='seats',
            new_name='seats_in_row',
        ),
    ]
