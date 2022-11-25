from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify


class User(AbstractUser):
   gender_choices =  (
      ('Male', 'Male'),
      ('Female', 'Female'),
      ('Other', 'Other'),
      ('not_saying', 'Prefer not to say'),      
   )
   profile_picture = models.ImageField(
      null=True,
      blank=True,
      upload_to='profile_images',
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg', 'webp'
            ]
         )
      ]
   )
   background_image = models.ImageField(
      null=True,
      blank=True,
      upload_to='profile_bg_images',
      validators=[
         FileExtensionValidator(  
            allowed_extensions=[
               'png', 'jpg', 'jpeg', 'webp'
            ]
         )
      ]
   )
   job_title = models.CharField(max_length=250, blank=True, null=True)
   bio = models.TextField(blank=True)
   city = models.CharField(max_length=100, blank=True, null=True)
   address = models.CharField(max_length=250, blank=True)
   mobile_no = models.CharField(max_length=14, blank=True)
   date_of_birth = models.DateField(null=True, blank=True)
   gender = models.CharField(max_length=50, choices=gender_choices, null=True)
   is_author = models.BooleanField(null=True, blank=True, default=False)
   slug = AutoSlugField(unique=True, populate_from='username', sep='_', null=True)


   def __str__(self):
      return f'{self.username}'

   def save(self, *args, **kwargs):
      self.slug = slugify(self.username)
      super().save(*args, **kwargs)

class UserSettings(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   request_author_access = models.BooleanField(null=True, blank=True, default=False)
   is_verified = models.BooleanField(null=True, blank=True, default=False)
   
   def __str__(self):
      return f'User settings for {self.user.username}'

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