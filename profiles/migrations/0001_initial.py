# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('date_birth', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('sexual_preference', models.CharField(blank=True, max_length=75)),
                ('country', models.CharField(max_length=75)),
                ('about_me', models.CharField(blank=True, max_length=250)),
                ('relationship_status', models.CharField(max_length=75)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
