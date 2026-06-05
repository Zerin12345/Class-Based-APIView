from django.urls import path
from API_app.views import *

urlpatterns = [
    path('students/', StudentAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    
]