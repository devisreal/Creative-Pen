from django.urls import path
from .views import single_post, PostDetailView
from pen_admin.views import categories

app_name = 'blog'

urlpatterns = [
   # path('<slug:slug>/', single_post, name='single_post'),   
   path('<slug:slug>/', PostDetailView.as_view(), name='single_post'),
]