# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom_app', '0002_auto_20170413_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='style',
            field=models.ManyToManyField(blank=True, null=True, to='newsroom_app.Style'),
        ),
    ]
