from typing import Any
from django import forms
from account.models import User, SocialHandle


class UserUpdateForm(forms.ModelForm):
   username = forms.CharField(
      label="",
      required=True,
      widget=forms.TextInput(
         attrs={
            "placeholder": "",            
            "class": "form-control",
            "id": "username",
            "type": "text",
         }
      ),
   )

   email = forms.EmailField(
      label="",
      required=True,
      widget=forms.EmailInput(
         attrs={
            "placeholder": "example@email.com",
            "class": "form-control",
            "id": "email",
            "type": "email",
         }
      ),
   )

   profile_picture = forms.ImageField(
      label="",
      required=False,
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "accept": "image/*",
            "class": "d-none",
            "id": "profile_picture",
            "onchange":"loadFile(event)"
         }
      ),
   )

   background_image = forms.ImageField(
      label="",
      required=False,
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
   )

   first_name = forms.CharField(
      label='',
      required=True,
      widget=forms.TextInput(
         attrs={
            "placeholder": "Firstname",
            "class": "form-control",
            "id": "first_name",
            "type": "text",
         }
      )
   )

   last_name = forms.CharField(
      label='',
      required=True,
      widget=forms.TextInput(
      attrs={
         "placeholder": "Lastname",
         "class": "form-control",
         "id": "last_name",
         "type": "text",
      }
      )
   )

   mobile_no = forms.CharField(
      label='',
      max_length=14,
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "+234...",             
            "class": "form-control",
            "id": "mobile_no",
            "maxlength": 14
         }
      )
   )   

   job_title = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
      attrs={
         "placeholder": "Position at ...",
         "class": "form-control",
         "id": "job_title",
         "type": "text",
      }
      )
   )

   bio = forms.CharField(
      label='',
      required=False,
      widget=forms.Textarea(
         attrs={
            "placeholder": "Brief description for your profile.",
            "class": "form-control  my-2",
            "id": "bio",
            "style": "height: 140px;resize: none;",
         }
      )
   )

   city = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
      attrs={
         "placeholder": "",
         "class": "form-control",
         "id": "city",
         "type": "text",
      }
      )
   )

   address = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
      attrs={
         "placeholder": "3 Saka Street, Lagos, Nigeria",
         "class": "form-control",
         "id": "address",
         "type": "text",
      }
      )
   )

   date_of_birth = forms.DateField(
      label="",
      required=False,
      widget=forms.DateInput(
         attrs={
            "type":"date",
            "class": "form-control profileDate bg-white",
            "placeholder":"Date of Birth",
            "id": 'date_of_birth'
         }
      )
   )

   gender_choices =  [
      ('Male', 'Male'),
      ('Female', 'Female'),
      ('Other', 'Other'),
      ('not_saying', 'Prefer not to say'),
   ]

   gender = forms.CharField(
      label='',
      required=False,      
      widget=forms.RadioSelect(
         choices=gender_choices,
         attrs={
            'class': '',
            'id': 'gender'
         }
      )
   )

   class Meta:
      model = User
      fields = (
         "username",
         "first_name",
         "last_name",
         "email",
         "profile_picture",
         "background_image",
         "job_title",
         "bio",
         "city",
         "address",
         "mobile_no",
         "date_of_birth",
         "gender",                  
      )

      def __init__(self, *args: Any, **kwargs: Any) -> None:
         super(UserUpdateForm, self).__init__(*args, **kwargs)

         for fieldname in (
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
            "background_image",
            "job_title",
            "bio",
            "city",
            "address",
            "mobile_no",
            "date_of_birth",
            "gender",  
         ):
            self.fields[fieldname].help_text = None

class UserSocialHandleForm(forms.ModelForm):

   facebook = forms.URLField(
      label='',
      required=False,
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.facebook.com/',
            "class": 'form-control  my-2',
            "id": 'facebook_handle'
         }
      )
   )

   linkedin = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.linkedin.com/',
            "class": 'form-control  my-2',
            "id": 'linkedin_handle'
         }
      )
   )

   twitter = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.twitter.com/ ',
            "class": 'form-control  my-2',
            "id": 'twitter_handle'
         }
      )
   )

   instagram = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.instagram.com/',
            "class": 'form-control  my-2',
            "id": 'instagram_handle'
         }
      )
   )

   youtube = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.youtube.com/',
            "class": 'form-control  my-2',
            "id": 'youtube_handle'
         }
      )
   )

   behance = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.behance.net/',
            "class": 'form-control  my-2',
            "id": 'behance_handle'
         }
      )
   )

   dribbble = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://dribbble.com/',
            "class": 'form-control  my-2',
            "id": 'dribbble_handle'
         }
      )
   )


   class Meta:
      model = SocialHandle
      fields = (
         'facebook',
         'linkedin',
         'twitter',
         'instagram',
         'youtube',
         'behance',
         'dribbble'
      )
      