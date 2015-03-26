# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='body',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='user',
        ),
    ]
