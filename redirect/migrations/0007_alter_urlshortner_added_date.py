# Generated by Django 4.1.2 on 2022-10-17 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0006_alter_urlshortner_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortner',
            name='added_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 17, 19, 12, 8, 746473)),
        ),
    ]
