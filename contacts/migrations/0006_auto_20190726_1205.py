# Generated by Django 2.2.3 on 2019-07-26 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_account_contacts'),
        ('contacts', '0005_auto_20190725_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='account',
        ),
        migrations.AddField(
            model_name='contact',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='accounts.Account'),
        ),
    ]
