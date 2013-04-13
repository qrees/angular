from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from gallery.views import AlbumDetail, AlbumList


urlpatterns = patterns('snippets.views',
    url(r'^$', AlbumList.as_view(), name="album-list"),
    url(r'^/(?P<pk>\w+)$', AlbumDetail.as_view(), name="album-details"),
)

urlpatterns = format_suffix_patterns(urlpatterns)