# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150718_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image_url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
