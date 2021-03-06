# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sphinxdoc.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(help_text='Used in the URL for the project. Must be unique.', unique=True)),
                ('path', models.CharField(help_text='Directory that contains Sphinx’ <tt>conf.py</tt>.', max_length=255, validators=[sphinxdoc.validators.validate_isdir])),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphinxdoc.Project'),
        ),
    ]
