from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from ..models import Language, Lead, Business, Genre
from .serializers import LeadSerializer, LanguageSerializer, BusinessSerializer, GenreSerializer

#Lead Views
class LeadCreateAPIView(CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadListAPIView(ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

#Language views
class LanguageCreateAPIView(CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageListAPIView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

#Business views
class BusinessCreateAPIView(CreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessListAPIView(ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

#Genre views
class GenreCreateAPIView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreListAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    