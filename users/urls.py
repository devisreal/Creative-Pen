from django.urls import path
from . import views
from pen_admin import views as admin_views


app_name = 'users'

urlpatterns = [   
   path('', views.dashboard, name="dashboard"),     
   path('profile/', views.user_profile, name="profile"),
   path('edit-profile/', views.edit_profile, name="edit_profile"),
   path('delete-account', views.delete_account, name='delete_account'),   


   # Admin Views
   path('staffs/', admin_views.staffs, name="staffs"),   
   path('staff__<str:username>/', admin_views.staff_single, name='single_staff'),
   path('authors/', admin_views.authors, name="authors"),   
   path('author__<str:username>/', admin_views.author_single, name='single_author'),
   path('readers/', admin_views.readers, name="readers"),
   path('reader__<str:username>/', admin_views.reader_single, name='single_reader'),
   path('subscribers/', admin_views.subscribers, name="subscribers"),
]