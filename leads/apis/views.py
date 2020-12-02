from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from ..models import Language, Lead, Business, Genre
from .serializers import LeadSerializer, LanguageSerializer, BusinessSerializer, GenreSerializer
from .permissions import IsAuthorOrStaff
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

#Lead Views
class LeadCreateAPIView(CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            serializer.save()

    def perform_update(self, serializer):
        serializer.save(partial=True)
        
class LeadListAPIView(ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def get_queryset(self):
        # if self.request.user.is_staff:
        #     return Lead.objects.all()
        # return Lead.objects.filter(user=self.request.user)
        return Lead.objects.all()


class LeadRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permissions_classes = (IsAuthorOrStaff,)

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
    