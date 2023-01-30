from django.urls import path
from .views import single_post, PostDetailView, edit_post
from pen_admin.views import categories

app_name = 'blog'

urlpatterns = [
   # path('<slug:slug>/', single_post, name='single_post'),   
   path('<slug:slug>/', PostDetailView.as_view(), name='single_post'),
   path('<slug:slug>/edit/', edit_post, name='edit_post'),

]