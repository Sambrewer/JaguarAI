# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0010_auto_20170410_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrowseNode',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parent', models.PositiveIntegerField(blank=True, null=True)),
                ('children', models.TextField(blank=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterModelOptions(
            name='search',
            options={'ordering': ('completed', 'id'), 'verbose_name_plural': 'Searches'},
        ),
        migrations.AlterModelOptions(
            name='supersearch',
            options={'ordering': ('-avg_revenue',), 'verbose_name_plural': 'Super Searches'},
        ),
        migrations.AddField(
            model_name='product',
            name='browse_nodes',
            field=models.ManyToManyField(blank=True, to='amazon.BrowseNode'),
        ),
    ]
