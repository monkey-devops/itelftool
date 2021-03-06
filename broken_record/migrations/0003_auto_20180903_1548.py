# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-03 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broken_record', '0002_auto_20180903_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokenrrecord',
            name='description',
            field=models.CharField(max_length=1024, verbose_name='故障描述'),
        ),
        migrations.AlterField(
            model_name='brokenrrecord',
            name='precaution',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='预防措施'),
        ),
        migrations.AlterField(
            model_name='brokenrrecord',
            name='process_description',
            field=models.TextField(max_length=1024, verbose_name='处理过程'),
        ),
    ]
