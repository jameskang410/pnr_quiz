# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PnrQuotes',
            fields=[
            ],
            options={
                'db_table': 'pnr_quotes',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
