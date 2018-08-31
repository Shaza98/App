# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-31 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=11)),
                ('age', models.IntegerField(max_length=11)),
                ('gender', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=30)),
            ],
        ),
    ]