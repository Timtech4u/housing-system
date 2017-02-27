# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('status', models.CharField(max_length=3, choices=[('ALA', 'ALLOCATED'), ('DEA', 'UNALLOCATED'), ('WAI', 'WAITING')])),
                ('house_code', models.CharField(max_length=50)),
                ('house_type', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('no_of_rooms', models.IntegerField()),
                ('year_of_lease', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Occupant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=50, blank=True, null=True)),
                ('second_name', models.CharField(max_length=50, blank=True, null=True)),
                ('position', models.CharField(max_length=50, blank=True, null=True)),
                ('marital_status', models.CharField(max_length=20, blank=True, null=True)),
                ('num_of_kids', models.IntegerField(blank=True, null=True)),
                ('tel_number', models.IntegerField(blank=True, null=True)),
                ('house', models.OneToOneField(to='allocate.House', blank=True, null=True)),
            ],
        ),
    ]
