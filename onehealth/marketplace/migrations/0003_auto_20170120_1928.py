# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-20 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_userapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppModelFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('field_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'app_model_fields',
                'verbose_name': 'AppModelField',
                'verbose_name_plural': 'AppModelFields',
            },
        ),
        migrations.CreateModel(
            name='AppModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('model_name', models.CharField(max_length=50)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.Apps')),
            ],
            options={
                'db_table': 'app_models',
                'verbose_name': 'AppModel',
                'verbose_name_plural': 'AppModels',
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('practo_account', models.PositiveIntegerField()),
                ('data_type', models.CharField(max_length=50)),
                ('data', models.TextField()),
                ('model_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.AppModelFields')),
            ],
            options={
                'db_table': 'user_data',
                'verbose_name': 'UserData',
                'verbose_name_plural': 'UserData',
            },
        ),
        migrations.AlterField(
            model_name='userapp',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='marketplace.Apps'),
        ),
        migrations.AddField(
            model_name='appmodelfields',
            name='app_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.AppModels'),
        ),
    ]
