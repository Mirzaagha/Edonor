# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-12 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='zipcode',
            field=models.CharField(default='91238', max_length=244),
        ),
    ]