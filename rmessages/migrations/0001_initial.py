# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ManyToManyField(related_name='receiver', to='profiles.UserProfile')),
                ('transmitter', models.ManyToManyField(related_name='transmitter', to='profiles.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
