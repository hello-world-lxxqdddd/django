# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-18 22:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileabout',
            old_name='emial',
            new_name='email',
        ),
    ]
