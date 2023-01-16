from django.urls import path
from . import views
from pen_admin import views as admin_views


app_name = 'users'

urlpatterns = [   
   path('dashboard/', views.dashboard, name="dashboard"),     
   path('request-access/<str:username>/', views.request_author_access, name="request_author_access"),
   path('bookmarks/', views.bookmarks, name="bookmarks"),
   path('bookmark/<int:id>/', views.bookmark_add, name='bookmark_add'),
   path('profile/', views.user_profile, name="profile"),      
   path('edit-profile/', views.edit_profile, name="edit_profile"),
   path('delete-account', views.delete_account, name='delete_account'),   


   # Admin Views
   path('staffs/', admin_views.staffs, name="staffs"),   
   path('staff__<str:username>/', admin_views.staff_single, name='single_staff'),
   path('block-staff/<str:username>/', admin_views.block_staff, name='block_staff'),
   path('unblock-staff/<str:username>/', admin_views.unblock_staff, name='unblock_staff'),
   path('revoke/<str:username>/', admin_views.revoke_staff_access, name='revoke_staff_access'),

   # Authors
   path('authors/', admin_views.authors, name="authors"),   
   path('author__<str:username>/', admin_views.author_single, name='single_author'),

   path('verify-author/<str:username>/', admin_views.verify_author, name='verify_author'),
   path('unverify-author/<str:username>/', admin_views.un_verify_author, name='unverify_author'),
   path('block-author/<str:username>/', admin_views.block_author, name='block_author'),
   path('unblock-author/<str:username>/', admin_views.unblock_author, name='unblock_author'),

   # ! Author Access
   path('authors/reject-access/<str:username>/', admin_views.reject_author_access, name='reject_author_access'),
   path('authors/accept-access/<str:username>/', admin_views.accept_author_access, name='accept_author_access'),

   # Readers
   path('readers/', admin_views.readers, name="readers"),
   path('reader__<str:username>/', admin_views.reader_single, name='single_reader'),
   path('block-reader/<str:username>/', admin_views.block_reader, name='block_reader'),
   path('unblock-reader/<str:username>/', admin_views.unblock_reader, name='unblock_reader'),

   # Subscribers
   path('subscribers/', admin_views.subscribers, name="subscribers"),
   path('subscriber/delete/<int:id>/', admin_views.delete_subscriber, name="delete_subscriber"),

   # Enquiries
   path('enquiries/', admin_views.enquiries, name="enquiries"),
   path('enquiry/<int:id>/', admin_views.single_enquiry, name='single_enquiry'),
   path('delete_enquiry/<int:id>/', admin_views.delete_enquiry, name='delete_enquiry'),

   # Categories
   path('categories/', admin_views.categories, name='categories'),
   path('category/<int:id>/edit/', admin_views.edit_category, name='edit_category'),
   path('delete_category/<int:id>/', admin_views.delete_category, name='delete_category'),
]