# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0029_search_last_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]