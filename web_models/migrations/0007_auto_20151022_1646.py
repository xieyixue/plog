# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0006_auto_20151022_1645'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]
