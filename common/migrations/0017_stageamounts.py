# Generated by Django 2.2.3 on 2019-07-30 09:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_auto_20190703_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='StageAmounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=100)),
                ('currencies', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=4), size=157), size=None)),
            ],
        ),
    ]