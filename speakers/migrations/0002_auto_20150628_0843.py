# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='name',
        ),
        migrations.AlterField(
            model_name='speaker',
            name='affiliation',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='pic',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'logo_images', blank=True),
        ),
    ]
