# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sub_users', models.ForeignKey(to='profiles.UserProfile', null=True, blank=True, related_name='to_user')),
                ('user', models.ForeignKey(related_name='from_user', to='profiles.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
