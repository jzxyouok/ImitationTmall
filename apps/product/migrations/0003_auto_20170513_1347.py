# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-13 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170506_0829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='propertyvalue',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Product',
            new_name='product',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='produceImage/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='type',
            field=models.CharField(choices=[('type_single', '\u6807\u9898'), ('type_detail', '\u8be6\u60c5')], max_length=100, verbose_name='\u56fe\u7247\u7c7b\u578b'),
        ),
    ]
