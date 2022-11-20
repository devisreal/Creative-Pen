from django.db import models


class ContactDetail(models.Model):
   name = models.CharField(max_length=100)
   subject = models.CharField(max_length=100)
   email_address = models.EmailField(max_length=255)
   message = models.TextField()
   date_posted = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'{self.name} on {self.date_posted}'


class Subscriber(models.Model):
   email = models.EmailField(max_length=255)
   date_subscribed = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.email