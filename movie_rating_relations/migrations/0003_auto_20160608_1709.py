# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 17:09
from __future__ import unicode_literals

from django.db import migrations
import csv


def add_rater_data(apps, schema_editor):
    Rater = apps.get_model("movie_rating_relations", "Rater")
    with open("user") as infile:
        read_file = csv.reader(infile, delimiter='|')
        for row in read_file:
            Rater.objects.create(user_id=row[0], age=row[1], gender=row[2], occupation=row[3], zipcode=row[4])


class Migration(migrations.Migration):

    dependencies = [
        ('movie_rating_relations', '0002_auto_20160608_1708'),
    ]

    operations = [
        migrations.RunPython(add_rater_data)
    ]