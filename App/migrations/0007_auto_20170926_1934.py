# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20170926_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='foto',
            field=models.ImageField(upload_to='media'),
        ),
    ]
