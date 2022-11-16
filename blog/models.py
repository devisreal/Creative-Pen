from django.db import models
from account.models import User
from django_quill.fields import QuillField
from django.core.validators import FileExtensionValidator
from taggit_selectize.managers import TaggableManager


class PostCategory(models.Model):
   name = models.CharField(max_length=150)
   category_image = models.ImageField(
      null=True,
      blank=True,
      upload_to='category_image',
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg', 'webp'
            ]
         )
      ]
   )
   date_created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name_plural = "Post Categories"


class Post(models.Model):
   post_types =  (      
      ('post', 'Post'),
      ('images', 'Images'),
      ('video', 'Video'),      
   )

   post_author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="Author")
   post_title = models.CharField(max_length=255)
   post_type = models.CharField(max_length=50, choices=post_types)
   short_description = models.TextField(null=True, blank=True)
   post_image = models.ImageField(
      null=True,
      blank=True,
      upload_to='post_images',
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg', 'webp'
            ]
         )
      ]
   )
   post_content = QuillField()
   category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
   tags = TaggableManager()
   is_featured = models.BooleanField(null=True, blank=True, default=False)
   date_posted = models.DateTimeField(auto_now_add=True)
   last_updated = models.DateField(auto_now=True)

   def __str__(self):
      return f'{self.post_title} by {self.post_author}'