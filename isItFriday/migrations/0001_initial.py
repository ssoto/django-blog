# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GifDate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('day_name', models.CharField(max_length=100)),
                ('day_of_week', models.IntegerField()),
                ('gif_url', models.CharField(max_length=300)),
            ],
        ),
    ]
