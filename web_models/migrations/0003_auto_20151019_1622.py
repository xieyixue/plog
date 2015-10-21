# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0002_urlcount_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlcount',
            name='create_at',
            field=models.CharField(max_length=500),
        ),
    ]
