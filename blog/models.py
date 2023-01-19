import readtime
from django.db import models
from account.models import User
from django.core.validators import FileExtensionValidator
from taggit_selectize.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from froala_editor.fields import FroalaField


class PostCategory(models.Model):
   name = models.CharField(max_length=150)
   color = models.CharField(max_length=20, default='blue', null=True, blank=True)
   emoji = models.CharField(max_length=5, null=True, blank=True)
   short_description = models.TextField(max_length=200, null=True, blank=True)
   category_image = models.ImageField(
      null=True,
      blank=True,
      upload_to='category_images/',
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg', 'webp'
            ]
         )
      ]
   )
   slug = AutoSlugField(unique=True, populate_from='name', sep='-', null=True)
   date_created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name

   def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)

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
      upload_to='posts/images',
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg', 'webp'
            ]
         )
      ]
   )
   post_video = models.FileField(
      upload_to='posts/videos',
      null=True,
      blank=True,
      validators=[
         FileExtensionValidator(
            allowed_extensions=['MOV','avi','mp4','webm','mkv']
         )
      ]
   )
   post_content = FroalaField(      
      theme='dark',
      null=True, blank=True
   )
   category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
   tags = TaggableManager()
   is_featured = models.BooleanField(null=True, blank=True, default=False)
   date_posted = models.DateTimeField(auto_now_add=True)
   last_updated = models.DateField(auto_now=True)
   slug = AutoSlugField(unique=True, populate_from='post_title', sep='-', null=True)
   hit_count_generic = GenericRelation(
      HitCount,
      object_id_field='object_pk',
      related_query_name='hit_count_generic_relation'
   )
   read_time = readtime.of_text(post_content).minutes
   bookmarks = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
   likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)

   def __str__(self):
      return f'{self.post_title} by {self.post_author}'
      
   def save(self, *args, **kwargs):
      self.slug = slugify(self.post_title)
      super().save(*args, **kwargs)
