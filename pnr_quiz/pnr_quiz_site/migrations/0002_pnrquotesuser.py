# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pnr_quiz_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PnrQuotesUser',
            fields=[
            ],
            options={
                'managed': False,
                'db_table': 'pnr_quotes_user',
            },
            bases=(models.Model,),
        ),
    ]
