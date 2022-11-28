from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
   path('', views.dashboard, name="dashboard"),
   path('profile/', views.user_profile, name="profile"),
   path('edit-profile/', views.edit_profile, name="edit_profile"),
   path('delete-account', views.delete_account, name='delete_account')
]