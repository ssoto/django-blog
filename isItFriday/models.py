"""
"""
from django.db import models


class GifDate(models.Model):
    day_name = models.CharField(max_length=100)
    day_of_week = models.IntegerField()
    gif_url = models.CharField(max_length=300)

    def __str__(self):
        return '%s - %s' % (self.day_name, self.day_of_week)
