# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocks', '0002_rock_refractive_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='rock',
            name='crystal_habit',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
