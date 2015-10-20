# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20151019_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='author',
        ),
    ]
