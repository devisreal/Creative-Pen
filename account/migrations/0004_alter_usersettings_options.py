# Generated by Django 4.0 on 2022-12-03 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_socialhandle_behance_socialhandle_dribbble_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersettings',
            options={'verbose_name': 'User Setting', 'verbose_name_plural': 'User Settings'},
        ),
    ]
