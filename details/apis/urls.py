from django.contrib import admin
from django.urls import path
from .views import DetailCreateAPIVIew, DetailListAPIView, DetailRUDAPIView

urlpatterns = [
    path("<int:pk>/", DetailRUDAPIView.as_view(), name="update-detail"),
    path("list/", DetailListAPIView.as_view(), name="list-details"),
]