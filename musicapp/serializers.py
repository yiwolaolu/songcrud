from rest_framework import serializers
from .models import Song, Artiste

class SongSerializer(serializers.ModelSeializer):
    class Meta:
        fields = (
            "id",
            "title",
            "date_released",
            "likes",
            "artiste_id",
            
        )
        model = Song
        
class ArtisteSerializer(serializers.ModelSeializer):
    class Meta:
        fields = (
            "id",
            "title",
            "date_released",
            "likes",
            "artiste_id",
            
        )
        model = Song        
        
        
        