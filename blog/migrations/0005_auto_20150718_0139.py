# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150718_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image_url',
            field=models.URLField(null=True, blank=True, default=''),
        ),
    ]
