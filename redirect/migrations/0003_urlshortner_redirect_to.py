# Generated by Django 4.1.2 on 2022-10-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0002_urlshortner'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortner',
            name='redirect_to',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]