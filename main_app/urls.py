from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('project/<int:project_id>/', views.project_detail, name='detail'),
]