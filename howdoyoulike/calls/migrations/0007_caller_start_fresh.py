# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0006_auto_20150208_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='caller',
            name='start_fresh',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
