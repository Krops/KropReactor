# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20170217_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]