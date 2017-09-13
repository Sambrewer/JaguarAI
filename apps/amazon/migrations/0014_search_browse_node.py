# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0013_browsenode_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='browse_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amazon.BrowseNode'),
        ),
    ]