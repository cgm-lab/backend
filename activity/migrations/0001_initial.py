# Generated by Django 3.1b1 on 2020-06-30 09:45

import common.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('guid', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('activity', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('location', models.CharField(blank=True, max_length=50)),
            ],
            bases=(common.models.BaseSheet, models.Model),
        ),
    ]
