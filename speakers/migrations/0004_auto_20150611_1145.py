# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0003_auto_20150610_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='pic',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'logo_images', blank=True),
        ),
    ]
