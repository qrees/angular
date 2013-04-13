from gallery.models import Album
from gallery.serializers import AlbumSerializer
from rest_framework import generics


class AlbumList(generics.ListCreateAPIView):
    model = Album
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Album
    serializer_class = AlbumSerializer