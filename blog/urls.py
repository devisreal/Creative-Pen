from django.urls import path
from .views import PostDetailView, edit_post, delete_post

app_name = 'blog'

urlpatterns = [   
   path('<slug:slug>/', PostDetailView.as_view(), name='single_post'),
   path('<slug:slug>/edit/', edit_post, name='edit_post'),
   path('<slug:slug>/delete/', delete_post, name='delete_post'),
]