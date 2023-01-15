# Generated by Django 4.0 on 2023-01-14 14:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_rename_post_bookmark_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
    ]
