# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0005_date_ipcount_pvforday_url_webserver_xurlcount'),
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
            name='XUrlCount',
        ),
    ]
