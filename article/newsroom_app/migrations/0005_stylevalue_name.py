# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom_app', '0004_auto_20170413_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylevalue',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]