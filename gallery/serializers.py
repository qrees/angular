from rest_framework import serializers
from gallery.models import Album

class AlbumSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Album