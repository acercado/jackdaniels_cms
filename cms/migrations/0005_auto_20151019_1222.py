# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20151019_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='author',
            field=models.CharField(max_length=200, default=timezone.now),
        ),
    ]
