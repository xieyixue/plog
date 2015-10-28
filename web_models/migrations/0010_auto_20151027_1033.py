# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0009_server'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xurlcount',
            name='date',
        ),
        migrations.RemoveField(
            model_name='xurlcount',
            name='url',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='Url',
        ),
        migrations.DeleteModel(
            name='XUrlCount',
        ),
    ]
