# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20150628_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='title',
            field=models.CharField(default='', max_length=128, blank=True),
            preserve_default=False,
        ),
    ]
