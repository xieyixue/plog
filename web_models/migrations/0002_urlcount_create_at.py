# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlcount',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 19, 1, 49, 36, 1833, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
