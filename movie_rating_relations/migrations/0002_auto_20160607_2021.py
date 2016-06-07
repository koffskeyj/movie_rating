# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_rating_relations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('time_stamp', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='user_id',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_id',
            new_name='item_id',
        ),
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.AddField(
            model_name='rating',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_rating_relations.Movie'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_rating_relations.Rater'),
        ),
    ]