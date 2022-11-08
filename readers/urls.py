from django.urls import path
from . import views

app_name = 'readers'

urlpatterns = [
   path('dashboard/', views.dashboard, name="dashboard"),
]