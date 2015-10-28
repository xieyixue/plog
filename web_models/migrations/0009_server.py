# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0008_date_url_xurlcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('port', models.IntegerField(default=22)),
                ('app', models.CharField(max_length=22)),
                ('path', models.FilePathField()),
                ('start', models.CharField(max_length=200)),
                ('stop', models.CharField(max_length=200)),
            ],
        ),
    ]
