from django.shortcuts import render
from .models import GifDate
from datetime import datetime


def today(request):
    t_date = datetime.today()
    gif_date = GifDate.objects.filter(day_of_week=t_date.weekday()).first()

    variables = {
        'week_day_name': gif_date.day_name,
        'image_url': gif_date.gif_url
    }
    return render(request,
                  'isItFriday/what_day_is_today.html',
                  variables)
