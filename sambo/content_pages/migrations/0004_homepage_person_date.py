# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-04 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_pages', '0003_homepage_person_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='person_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата на сотруднике'),
        ),
    ]