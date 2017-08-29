# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restshop', '0010_auto_20170829_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='restshop.Seller'),
            preserve_default=False,
        ),
    ]