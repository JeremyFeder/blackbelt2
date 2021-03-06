# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-05 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest', models.CharField(max_length=45)),
                ('addby', models.CharField(max_length=45)),
                ('plan', models.CharField(max_length=144)),
                ('trav_start', models.DateTimeField()),
                ('trav_end', models.DateTimeField()),
                ('dateadd', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_reg.User')),
                ('users', models.ManyToManyField(related_name='items', to='login_reg.User')),
            ],
        ),
    ]
