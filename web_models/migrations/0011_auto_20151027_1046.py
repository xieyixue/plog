# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0010_auto_20151027_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='path',
            field=models.CharField(max_length=200),
        ),
    ]
