# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=30, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
