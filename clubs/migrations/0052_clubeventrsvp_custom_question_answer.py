# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-22 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0051_clubevent_custom_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubeventrsvp',
            name='custom_question_answer',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]