# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-01 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20180101_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='answer_7_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='answer_7_1_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='answer_7_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='answer_7_2_check',
            field=models.BooleanField(default=False),
        ),
    ]
