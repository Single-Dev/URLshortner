# Generated by Django 4.1.2 on 2022-10-17 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0004_remove_urlshortner_redirect_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortner',
            name='added_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 17, 19, 9, 59, 549248)),
        ),
    ]
