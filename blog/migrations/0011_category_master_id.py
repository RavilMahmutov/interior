# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_category_name_of_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='master_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='blog.Category', related_name='parrent'),
        ),
    ]
