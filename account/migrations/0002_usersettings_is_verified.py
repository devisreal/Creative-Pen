# Generated by Django 4.0 on 2022-11-22 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
