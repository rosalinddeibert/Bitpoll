# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import dudel.base.validators


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dudeluser',
            name='timezone',
            field=models.CharField(default='UTC', max_length=40, validators=[dudel.base.validators.validate_timezone]),
        ),
    ]
