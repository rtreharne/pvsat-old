# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forename', models.CharField(unique=True, max_length=128)),
                ('surname', models.CharField(unique=True, max_length=128)),
                ('affiliation', models.CharField(unique=True, max_length=128)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('url', models.URLField()),
                ('pic', models.ImageField(upload_to=b'logo_images', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
