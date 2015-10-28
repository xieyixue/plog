# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0004_auto_20151019_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='IPCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=500)),
                ('count', models.IntegerField()),
                ('date', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PVForDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('time', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WebServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=200)),
                ('port', models.IntegerField()),
                ('url', models.URLField()),
                ('app', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='XUrlCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('date', models.ForeignKey(to='web_models.Date')),
                ('url', models.ForeignKey(to='web_models.Url')),
            ],
        ),
    ]
