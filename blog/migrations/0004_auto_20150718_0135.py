# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_entry_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image_url',
            field=models.URLField(null=True, blank=True, default=None),
        ),
    ]
