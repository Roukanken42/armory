# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20170328_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(null=True)),
                ('crystalslots', models.IntegerField(null=True)),
                ('defence', models.IntegerField(null=True)),
                ('impact', models.IntegerField(null=True)),
                ('attack', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='itemdata',
            name='enchantEnable',
        ),
        migrations.RemoveField(
            model_name='itemdata',
            name='rareGrade',
        ),
        migrations.AddField(
            model_name='itemdata',
            name='enchantable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemdata',
            name='rarity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='itemdata',
            name='equipmentData',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.EquipmentData'),
        ),
    ]
