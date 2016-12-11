"""
"""
from django.db import models


class OnlineGif(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class GifDate(models.Model):
    day_name = models.CharField(max_length=100)
    day_of_week = models.IntegerField()
    gif_urls = models.ManyToManyField(OnlineGif)

    class Meta:
        ordering = ('day_of_week',)

    def __str__(self):
        return '%s - %s' % (self.day_name, self.day_of_week)
