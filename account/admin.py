from django.contrib import admin
from .models import User, UserSettings, SocialHandle

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ('username', 'email', 'first_name', 'last_name')
   search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
   pass   

@admin.register(SocialHandle)
class SocialHandleAdmin(admin.ModelAdmin):
   pass