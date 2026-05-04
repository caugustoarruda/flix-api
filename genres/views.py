from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalPermissionClass

  
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer