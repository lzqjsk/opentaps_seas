# Generated by Django 2.2.10 on 2020-03-25 16:36

import cratedb.fields.array
import cratedb.fields.hstore
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_auto_20200309_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterrateplanhistory',
            name='rate_details',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Rate Details'),
        ),
    ]