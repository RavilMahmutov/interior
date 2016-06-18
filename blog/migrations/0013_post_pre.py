# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160519_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pre',
            field=models.TextField(blank=True, null=True),
        ),
    ]
