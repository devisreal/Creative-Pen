# Generated by Django 4.0 on 2023-01-24 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_rename_request_author_access_date_usersettings_requested_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, null=True),
        ),
    ]
