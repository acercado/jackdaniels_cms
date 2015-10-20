# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_remove_locations_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='schedule',
            field=models.TextField(),
        ),
    ]
