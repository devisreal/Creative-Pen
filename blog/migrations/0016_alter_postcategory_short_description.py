# Generated by Django 4.0 on 2023-01-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_rename_favourites_post_bookmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategory',
            name='short_description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
