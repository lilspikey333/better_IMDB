# Generated by Django 3.0.3 on 2020-02-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('better_IMDB', '0006_movie_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(related_name='movies', to='better_IMDB.Genre'),
        ),
    ]