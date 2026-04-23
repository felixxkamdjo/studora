from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:project_pk>/', views.apply, name='apply'),
    path('my/', views.my_applications, name='my_applications'),
    path('<int:pk>/review/', views.review_application, name='review_application'),
]