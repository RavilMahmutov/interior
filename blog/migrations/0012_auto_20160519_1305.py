# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_category_master_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='master_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='subcats', to='blog.Category'),
        ),
    ]
