import random
from django.shortcuts import render
from .models import GifDate
from datetime import datetime


def today(request):
    t_date = datetime.today()
    gif_date = GifDate.objects.filter(day_of_week=t_date.weekday()).first()

    urls = gif_date.gif_urls.all()
    image_url = urls[
        random.randint(0, len(urls) - 1)
    ].url

    variables = {
        'week_day_name': gif_date.day_name,
        'image_url': image_url
    }
    return render(request,
                  'isItFriday/what_day_is_today.html',
                  variables)
