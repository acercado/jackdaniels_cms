# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20151019_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='location',
        ),
        migrations.AddField(
            model_name='locations',
            name='author',
            field=models.CharField(max_length=200, default='abc'),
        ),
    ]
