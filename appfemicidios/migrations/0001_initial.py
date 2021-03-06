# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-07 05:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Femicidio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.IntegerField(blank=True)),
                ('country', models.TextField()),
                ('province', models.TextField()),
                ('city', models.TextField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
