# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_auto_20151107_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='score',
        ),
    ]
