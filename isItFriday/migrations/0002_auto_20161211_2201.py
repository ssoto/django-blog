# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isItFriday', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineGif',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('url', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='gifdate',
            name='gif_url',
        ),
        migrations.AddField(
            model_name='gifdate',
            name='gif_urls',
            field=models.ManyToManyField(to='isItFriday.OnlineGif'),
        ),
    ]
