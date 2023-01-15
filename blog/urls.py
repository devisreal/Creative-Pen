from django.urls import path
from . import views
from pen_admin.views import categories

app_name = 'blog'

urlpatterns = [
   path('<slug:slug>/', views.single_post, name='single_post'),   
]