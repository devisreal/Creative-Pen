from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('footer/', views.footer, name="footer"),
    path('latest/', views.latest_posts, name="latest_posts"),
    path('about/', views.about, name="about"),
    path('categories/', views.categories, name="categories"),
    path('category/<slug:slug>/', views.single_category, name='category'),
    path('contact/', views.contact, name="contact"),
    path('search', views.search_posts, name="search"),
    path('404/', views.error_page, name='error_page')
]
