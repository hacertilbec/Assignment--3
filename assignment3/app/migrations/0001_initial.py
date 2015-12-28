# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=70)),
                ('code', models.CharField(blank=True, max_length=20)),
                ('classroom', models.CharField(blank=True, max_length=20)),
                ('times', models.CharField(blank=True, max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=30)),
                ('lastName', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=30)),
                ('lastName', models.CharField(blank=True, max_length=30)),
                ('office_details', models.CharField(blank=True, max_length=200)),
                ('phone_number', models.CharField(max_length=11)),
                ('email', models.EmailField(blank=True, max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(null=True, to='app.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Teacher'),
        ),
    ]
