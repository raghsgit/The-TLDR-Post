# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-09 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarize', '0008_auto_20171009_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsslinks',
            name='number_of_feeds',
            field=models.PositiveIntegerField(default=3),
        ),
    ]
