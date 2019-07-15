# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-03 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_accessoriesprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='pipes_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
