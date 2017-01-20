# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-20 11:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import marketplace.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('version_number', models.DecimalField(decimal_places=6, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('build', models.FileField(upload_to=marketplace.models.upload_build)),
                ('webhook', models.URLField()),
            ],
            options={
                'db_table': 'apps',
                'verbose_name': 'App',
                'verbose_name_plural': 'Apps',
            },
        ),
    ]