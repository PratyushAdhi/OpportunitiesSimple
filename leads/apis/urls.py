from django.contrib import admin
from django.urls import path
from .views import (LeadCreateAPIView, LeadListAPIView, LeadRUDAPIView,
                    GenreCreateAPIView, GenreListAPIView, GenreRUDAPIView,
                    BusinessCreateAPIView, BusinessListAPIView, BusinessRUDAPIView,
                    LanguageCreateAPIView, LanguageListAPIView, LanguageRUDAPIView)


urlpatterns = [
    path("leads/", LeadListAPIView.as_view(), name="list-leads"),
    path("leads/create/", LeadCreateAPIView.as_view(), name="lead-create"),
    path("leads/<int:pk>/", LeadRUDAPIView.as_view(), name="lead-rud"),
    path("languages/create/", LanguageCreateAPIView.as_view(), name="language-create"),
    path("languages/<int:pk>/", LanguageRUDAPIView.as_view(), name="language-rud"),
    path("business/create/", BusinessCreateAPIView.as_view(), name="business-create"),
    path("business/<int:pk>/", BusinessRUDAPIView.as_view(), name="business-rud"),
    path("genre/create/", GenreCreateAPIView.as_view(),name="genre-create"),
    path("genre/<int:pk>/", GenreRUDAPIView.as_view(), name="genre-rud"),
    
]
