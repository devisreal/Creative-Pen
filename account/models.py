from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


class User(AbstractUser):
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
   bio = models.TextField(blank=True)
   address = models.CharField(max_length=250, blank=True)
   mobile_no = models.CharField(max_length=14, blank=True)
   date_of_birth = models.DateField(null=True, blank=True)
   is_author = models.BooleanField(null=True, blank=True, default=False)
   slug = AutoSlugField(unique=True, populate_from='username', sep='_', null=True)


   def __str__(self):
      return f'{self.username}'



class UserSettings(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   request_author_access = models.BooleanField(null=True, blank=True, default=False)
   
   def __str__(self):
      return f'User settings for {self.user.username}'