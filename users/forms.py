from typing import Any
from django import forms
from account.models import User


class UserUpdateForm(forms.ModelForm):
   username = forms.CharField(
      label="",
      widget=forms.TextInput(
         attrs={
            "placeholder": "",
            "class": "form-control bg-light",
            "id": "username",
            "type": "text",
         }
      ),
   )

   email = forms.EmailField(
      label="",
      widget=forms.EmailInput(
         attrs={
            "type": "email",
            "placeholder": "",
            "class": "form-control bg-light",
            "id": "email",
         }
      ),
   )

   image = forms.ImageField(
      label='',
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "class": "form-control bg-light",
            "id": "image"
         }
      )
   )

   first_name = forms.CharField(
      widget=forms.TextInput(
      attrs={
            "placeholder": "",
            "class": "form-control bg-light",
            "id": "firstname",
            "type": "text"
         }
      )
   )

   last_name = forms.CharField(
      widget=forms.TextInput(
         attrs={
            "placeholder": "",
            "class": "form-control bg-light",
            "id": "lastname",
            "type": "text"
         }
      )
   )

   phone = forms.CharField(
      widget=forms.NumberInput(
         attrs={
            "placeholder": "Phone Number",
            "class": "form-control bg-light",
            "type": "tel"
         }
      )
   )

   bio = forms.CharField(
      widget=forms.Textarea(
         attrs={
            "placeholder": "Write About yourself",
            "class": "form-control bg-light",
            "id": "ProfileBio",
            'style': 'height: 120px'
         }
      )
   )


   class Meta:
      model = User
      fields = ("username", "email")
      # fields = ('image', 'first_name', 'last_name', 'phone', 'bio')

   def __init__(self, *args: Any, **kwargs: Any) -> None:
      super(UserUpdateForm, self).__init__(*args, **kwargs)

      for fieldname in (
         "username",
         "email",
      ):
         self.fields[fieldname].help_text = None
