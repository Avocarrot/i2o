# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=1023)),
                ('condition', models.CharField(max_length=3, choices=[(b'GT', b'Greater than'), (b'GTE', b'Greater than or equal'), (b'LT', b'Less than'), (b'LTE', b'Less than or equal'), (b'EQ', b'Equal')])),
            ],
        ),
        migrations.CreateModel(
            name='TextToSpeechAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='texttospeechaction',
            name='trigger',
            field=models.ForeignKey(related_name='actions', to='actions.Trigger'),
        ),
        migrations.AddField(
            model_name='condition',
            name='trigger',
            field=models.ForeignKey(related_name='conditions', to='actions.Trigger'),
        ),
    ]
