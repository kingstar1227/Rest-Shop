# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restshop', '0004_auto_20170828_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
