# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-05 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handout',
            name='prob_url',
            field=models.CharField(blank=True, help_text='The URL for the problems handout', max_length=255),
        ),
        migrations.AlterField(
            model_name='handout',
            name='soln_url',
            field=models.CharField(blank=True, help_text='The URL for the solutions handout', max_length=255),
        ),
    ]