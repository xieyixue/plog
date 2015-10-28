# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0011_auto_20151027_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='url',
            field=models.URLField(default=b'127.0.0.1:8080'),
        ),
    ]
