# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 17:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vine', '0002_auto_20171116_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vineitem',
            name='index',
        ),
    ]
