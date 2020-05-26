from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('resume/', views.resume, name='resume'),
    path('project/<int:project_id>/', views.project_detail, name='detail'),
]
