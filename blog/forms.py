from django import forms
from .models import PostCategory, Post, Comment
from taggit.forms import TagField, TagWidget
from froala_editor.widgets import FroalaEditor
from django.core.validators import FileExtensionValidator

class AddCategoryForm(forms.ModelForm):
   name =  forms.CharField(
      label='Category Name',
      widget=forms.TextInput(
         attrs={
            "placeholder": "category x", 
            "class": "form-control",
            "id": "category_name"
         }
      )
   )
   color =  forms.CharField(
      label='Category Color',      
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "danger, primary, info ...", 
            "class": "form-control",            
            "id": "category_color"
         }
      )
   )
   emoji =  forms.CharField(
      label='Category Emoji',
      required=False,
      max_length=3,
      widget=forms.TextInput(
         attrs={
            "placeholder": "🐛", 
            "class": "form-control",
            "id": "category_emoji"
         }
      )
   )
   short_description = forms.CharField(
      label='Short description',
      required=False,
      widget=forms.Textarea(
         attrs={
            'placeholder': 'Short description about this category ...',
            'class': 'form-control text-md border-2',
            'id': 'short_description',
            'style': 'height: 70px;resize:none;'
         }
      )
   )
   category_image = forms.ImageField(
      label='Category Image',
      required=False,
      widget=forms.FileInput(         
         attrs={
            "placeholder": "",
            "class": "d-none",
            "id": "category_image",
            "onchange":"loadBgFile(event)"
         }
      )
   )
   class Meta:
      model = PostCategory
      fields = (
         'name', 
         'color', 
         'emoji',
         'short_description', 
         'category_image'
      )

class CreatePostForm(forms.ModelForm):
   post_title = forms.CharField(
      label='Post Title',       
      widget=forms.TextInput(
         attrs={
            "placeholder": "Post title", 
            "class": "form-control",
            "id": "post_title"
         }
      )
   )
   post_types =  (      
      ('post', 'Post'),
      ('images', 'Images'),
      ('video', 'Video'),  
   )
   post_type = forms.CharField(
      label='',
      required=True,
      widget=forms.RadioSelect(
         choices=post_types,
         attrs={
            'class': '',
            'id': 'post_type'
         }
      )
   )
   short_description = forms.CharField(
      label='Short description',
      widget=forms.Textarea(
         attrs={
            'placeholder': 'Short description about your post ...',
            'class': 'form-control text-md mb-3 border-2',
            'id': 'short_description',
            'style': 'height: 140px;resize:none;'
         }
      )
   )
   post_image = forms.ImageField(
      label="Post Image",
      help_text='Note: Only JPG, JPEG and PNG. Our suggested dimension is landscape. Other dimensions will be cropped to fit our thumbnails',
      required=True,
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "accept": "image/*",
            "class": "d-none",
            "id": "background_image",
            "onchange":"loadBgFile(event)"
         }
      ),
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg', 'webp'
            ]
         )
      ]
   )
   post_content = forms.CharField(
      label='Post content',
      widget=FroalaEditor(
         
      )
   )
   category = forms.ModelChoiceField(
      label='Post category',
      queryset=PostCategory.objects.all(),
      widget=forms.Select(         
         attrs={
            'placeholder': '',
            'class': 'form-select text-md border-2 mb-3',
         }
      )
   )
   tags = TagField(
      label='Tags',  
      required=False,    
      help_text='Maximum of 6 keywords. Keywords should all be in lowercase and separated by commas.',
      widget=TagWidget(
         attrs={
            "placeholder": "Enter post tags", 
            "class": "form-control border-0",
            "id": "inputTags",                
         }            
      )
   )   
   is_featured = forms.BooleanField(
      label='Featured post ?',
      required=False,
      widget=forms.CheckboxInput(         
         attrs={
            'class': 'form-check-input',
            'id': 'is_featured'
         }
      )
   )
   class Meta:
      model = Post
      fields = (
         'post_title',
         'post_type',
         'short_description',
         'post_image',         
         'post_content',
         'category',
         'tags',
         'is_featured'
      )           

class CommentForm(forms.ModelForm):
   comment = forms.CharField(
      widget=forms.Textarea(
         attrs={            
            'class': 'form-control',
            'rows': '5'
         }
      )
   )

   class Meta:
      model = Comment
      fields = ('comment',)
