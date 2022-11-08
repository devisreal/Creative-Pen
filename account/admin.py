from django.contrib import admin
from .models import User, UserSettings

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ('username', 'email', 'first_name', 'last_name')
   search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
   pass   