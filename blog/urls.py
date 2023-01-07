from django.urls import path
from . import views
from pen_admin.views import categories

app_name = 'blog'

urlpatterns = [
   path('post/', views.single_post, name='single_post' ),
   path('create-post/', views.create_post, name='create_post'),   
]