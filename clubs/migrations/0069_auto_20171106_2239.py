# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-07 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0068_club_bcg_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='bcg_template',
        ),
        migrations.AddField(
            model_name='club',
            name='bcg_style',
            field=models.BooleanField(default=False, help_text='Use CMS style page like bcg?'),
        ),
    ]
