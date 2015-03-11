# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_registro_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='edad',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='nick',
            field=models.CharField(default='xxx', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='password',
            field=models.CharField(default='xxx', max_length=15),
            preserve_default=False,
        ),
    ]
