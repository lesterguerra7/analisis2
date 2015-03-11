# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='usuario',
            field=models.CharField(default='xxx', max_length=50),
            preserve_default=False,
        ),
    ]
