# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-02 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accessories_size',
            new_name='AccessoriesSize',
        ),
        migrations.RenameModel(
            old_name='Accessories_type',
            new_name='AccessoriesType',
        ),
        migrations.RemoveField(
            model_name='accessories',
            name='pipe_type',
        ),
        migrations.DeleteModel(
            name='Pipes',
        ),
    ]
