# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-25 12:23
from __future__ import unicode_literals

import apps.user_main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='image',
            field=models.ImageField(default='static/img/2.png', storage=apps.user_main.models.ImageStorage(), upload_to='upload/img/%Y%m%d'),
        ),
    ]
