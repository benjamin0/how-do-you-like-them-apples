# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0003_auto_20150207_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='answer_text',
            new_name='choice_text',
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(related_name='choices', to='calls.Question'),
            preserve_default=True,
        ),
    ]
