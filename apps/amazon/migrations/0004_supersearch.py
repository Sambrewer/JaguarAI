# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0003_auto_20170330_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('products', models.ManyToManyField(blank=True, to='amazon.Product')),
                ('searches', models.ManyToManyField(blank=True, to='amazon.Search')),
            ],
        ),
    ]
