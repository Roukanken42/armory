# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 12:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0022_auto_20170416_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemdata',
            old_name='equip',
            new_name='equipment',
        ),
    ]
