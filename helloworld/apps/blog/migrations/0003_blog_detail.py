# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-28 18:42
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170818_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u6587\u7ae0\u5185\u5bb9\t'),
        ),
    ]
