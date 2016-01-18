# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('last_sale', models.FloatField()),
                ('market_cap', models.FloatField()),
                ('ipo', models.IntegerField()),
                ('sector', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('summary_quote', models.URLField()),
            ],
        ),
    ]
