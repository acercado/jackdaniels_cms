# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('schedule', models.DateTimeField()),
                ('address', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('info', models.TextField()),
                ('banner', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.ForeignKey(to='cms.Locations')),
            ],
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('info', models.TextField()),
                ('banner', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.ForeignKey(to='cms.Locations')),
                ('tag_account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respondents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('answer', models.ForeignKey(to='cms.Answers')),
            ],
        ),
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField(max_length=200)),
                ('info', models.TextField()),
                ('reward_type', models.CharField(default='p', max_length=1, choices=[('r', 'Redeemable'), ('p', 'Points')])),
                ('reward_value', models.IntegerField(default=0)),
                ('banner', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='contests',
            old_name='publish_schedule',
            new_name='publish_duration',
        ),
        migrations.RenameField(
            model_name='contests',
            old_name='created_date',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='contests',
            name='banner',
            field=models.CharField(default=datetime.datetime(2015, 10, 15, 9, 21, 16, 165255, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contests',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondents',
            name='contest',
            field=models.ForeignKey(to='cms.Contests'),
        ),
    ]
