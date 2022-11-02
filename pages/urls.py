from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('latest/', views.latest, name="latest_posts"),
   path('about/', views.about, name="about"),
   path('categories/', views.categories, name="categories"),
   path('contact/', views.contact, name="contact")
]