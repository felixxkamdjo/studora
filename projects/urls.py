from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list_student, name='project_list_student'),
    path('teacher/', views.project_list_teacher, name='project_list_teacher'),
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
]