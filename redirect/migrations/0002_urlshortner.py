# Generated by Django 4.1.2 on 2022-10-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLshortner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=75)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]