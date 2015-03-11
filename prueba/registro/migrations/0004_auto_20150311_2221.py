# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20150311_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='nick',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='password',
        ),
    ]
