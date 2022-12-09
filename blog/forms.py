from django import forms
from .models import PostCategory, Post
from taggit.forms import TagField, TagWidget

class CreatePostForm(forms.ModelForm):
   
   tags = TagField(
      help_text='Enter max of 6 characters',
         widget=TagWidget(
            attrs={
               "class": "tags-field form-control",
               "id": "inputTags",                
            }            
         )
   )

   class Meta:
      model = Post
      fields = '__all__'
   