# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0003_speaker_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
