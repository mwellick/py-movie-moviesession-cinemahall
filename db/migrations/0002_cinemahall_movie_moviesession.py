# Generated by Django 4.0.2 on 2024-04-15 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rows', models.IntegerField()),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('actors', models.ManyToManyField(related_name='movies', to='db.Actor')),
                ('genres', models.ManyToManyField(related_name='movie_genre', to='db.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='MovieSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField(auto_now_add=True)),
                ('cinema_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session', to='db.cinemahall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_info', to='db.movie')),
            ],
        ),
    ]
