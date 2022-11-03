from rest_framework import generics

from .models import Song, Artiste
from .serializers import SongSerializer, ArtisteSerializer

class Songlist(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.object.all()
    serializer_class = SongSerializer

class Artistelist(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    
class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.object.all()
    serializer_class = ArtisteSerializer
