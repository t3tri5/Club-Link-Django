# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-08 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0034_auto_20170608_0702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubnews',
            options={'ordering': ('-publish_date',)},
        ),
    ]
