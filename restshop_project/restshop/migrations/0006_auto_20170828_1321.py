# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restshop', '0005_productimage_is_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['product__title', '-is_main', 'image']},
        ),
    ]