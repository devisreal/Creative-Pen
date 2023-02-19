from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify

class User(AbstractUser):
    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),        
    )
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_images",
        validators=[
            FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg", "webp"])
        ],
    )
    background_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_bg_images",
        validators=[
            FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg", "webp"])
        ],
    )
    job_title = models.CharField(max_length=250, blank=True, null=True)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True)
    mobile_no = models.CharField(max_length=14, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=gender_choices, null=True)
    is_author = models.BooleanField(blank=True, default=False)    
    slug = AutoSlugField(unique=True, populate_from="username", sep="_", null=True)

    def initials(self):
        x = self.get_full_name()
        fullname = str(x)
        l = [] 
        for i in fullname.split(' '): 
            l.append(i[0]) 
        result = ".".join(l) + '.'
        return result
        
    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

@receiver(pre_delete, sender=User)
def user_image_delete(sender, instance, **kwargs):
    instance.file.delete(False)

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='following', default=None, blank=True)
    request_author_access = models.BooleanField(blank=True, default=False)
    requested_date = models.DateTimeField(null=True, blank=True)
    accepted_date = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return f"User settings for {self.user.username}"

    class Meta:
        verbose_name = "User Setting"
        verbose_name_plural = "User Settings"

class SocialHandle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    behance = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Social Handles"