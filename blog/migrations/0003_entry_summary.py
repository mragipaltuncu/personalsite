# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_entry_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='summary',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
    ]
