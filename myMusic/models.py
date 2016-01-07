from django.db import models

from django.template.defaultfilters import slugify


class Playlist(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Playlist, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Song(models.Model):
    playlist = models.ForeignKey(Playlist)

    name = models.CharField(max_length=256)
    url = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
