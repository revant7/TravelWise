from django.contrib import admin
from django.urls import path, include
from Home import views


urlpatterns = [
    path("student", views.StudentListAPIView.as_view(), name="student"),
]
