from django.contrib import admin
from . import models


@admin.register(models.PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
   list_display = ('name',)

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
   list_display = ('post_title','post_author', 'is_featured')
   list_per_page = 15 
   search_fields = ('post_title', 'post_author', 'category')
   list_editable = ['is_featured']
   def get_queryset(self, request):
      return super().get_queryset(request).prefetch_related('tags')

   def tag_list(self, obj):
      return u", ".join(o.name for o in obj.tags.all())   

"""
! list_per_page = 10
! search_fields = ['title']
! list_editable = ['unit_price']

"""

