# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0005_auto_20150208_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='caller',
            name='end_num',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caller',
            name='start_num',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
