# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0003_auto_20151019_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlcount',
            old_name='create_at',
            new_name='date',
        ),
    ]
