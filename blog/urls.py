from django.urls import path
from .views import create_post

app_name = 'blog'

urlpatterns = [
   path('create-post/', create_post, name='create_post')
]