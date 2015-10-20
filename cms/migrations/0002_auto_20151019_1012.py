# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locations',
            options={'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='promotions',
            options={'verbose_name_plural': 'Promotions'},
        ),
        migrations.AlterModelOptions(
            name='respondents',
            options={'verbose_name_plural': 'Respondents'},
        ),
        migrations.AlterModelOptions(
            name='rewards',
            options={'verbose_name_plural': 'Rewards'},
        ),
    ]
