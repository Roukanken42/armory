# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0021_auto_20170416_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemdata',
            old_name='equipdata',
            new_name='equip',
        ),
    ]
