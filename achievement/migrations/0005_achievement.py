# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-21 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0010_auto_20170519_1849'),
        ('achievement', '0004_auto_20170520_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.DateTimeField()),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.AchievementData')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gear.Player')),
            ],
        ),
    ]
