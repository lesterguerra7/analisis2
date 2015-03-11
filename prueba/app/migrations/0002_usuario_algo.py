# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='algo',
            field=models.CharField(default=datetime.datetime(2015, 2, 11, 21, 14, 57, 416242, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
