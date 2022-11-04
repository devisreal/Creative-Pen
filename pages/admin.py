from django.contrib import admin
from . import models


@admin.register(models.ContactDetail)
class ContactFormAdmin(admin.ModelAdmin):
   list_display = ('firstname', 'lastname', 'date_posted')

@admin.register(models.Subscriber)
class SubscribersAdmin(admin.ModelAdmin):
   list_display = ('email',)

