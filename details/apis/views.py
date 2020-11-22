from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DetailSerializer
from ..models import Detail
from .permissions import IsAuthorOrStaff

class DetailCreateAPIVIew(CreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class DetailListAPIView(ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Detail.objects.all()
        else:
            return Detail.objects.filter(user=self.request.user)

class DetailRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    permissions_classes = (IsAuthorOrStaff,)

    
        