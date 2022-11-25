from .models import User, UserSettings, SocialHandle
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args , **kwargs):
    if created:
        UserSettings.objects.create(user=instance)
        SocialHandle.objects.create(user=instance)
