# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20160425_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('definition', models.TextField(blank=True)),
                ('language', models.CharField(max_length=25)),
                ('antonyms', models.ManyToManyField(blank=True, related_name='_word_antonyms_+', to='dictionary.Word')),
                ('synonyms', models.ManyToManyField(blank=True, related_name='_word_synonyms_+', to='dictionary.Word')),
                ('translaions', models.ManyToManyField(blank=True, related_name='_word_translaions_+', to='dictionary.Word')),
            ],
        ),
        migrations.RemoveField(
            model_name='words',
            name='antonyms',
        ),
        migrations.RemoveField(
            model_name='words',
            name='synonyms',
        ),
        migrations.RemoveField(
            model_name='words',
            name='translation',
        ),
        migrations.DeleteModel(
            name='Words',
        ),
    ]
