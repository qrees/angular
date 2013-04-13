from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('album-details', args=(self.pk,))

