from django.urls import path
from . import views

app_name = 'pen_admin'

urlpatterns = [
   path('', views.admin_dashboard, name="dashboard"),
   
]