# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='.')),
                ('name', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
