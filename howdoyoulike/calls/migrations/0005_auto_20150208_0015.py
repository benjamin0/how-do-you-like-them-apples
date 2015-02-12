# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0004_auto_20150207_2243'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Intro',
        ),
        migrations.AddField(
            model_name='caller',
            name='intro_text',
            field=models.CharField(default='abc', max_length=1600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caller',
            name='outro_text',
            field=models.CharField(default=b'abc', max_length=1600),
            preserve_default=False,
        ),
    ]
