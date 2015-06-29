# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_auto_20150629_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='linkedin',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='twitter',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
    ]
