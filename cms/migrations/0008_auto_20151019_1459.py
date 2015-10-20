# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20151019_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='locations',
            name='schedule',
            field=models.CharField(max_length=200),
        ),
    ]
