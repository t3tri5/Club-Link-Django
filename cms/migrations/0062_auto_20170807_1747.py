# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-07 21:47
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0061_auto_20170807_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubpage',
            name='visibility',
            field=models.IntegerField(choices=[(0, 'Everyone'), (1, 'Members Only'), (2, 'Non-Members Only'), (3, 'None')], default=0),
        ),
    ]
