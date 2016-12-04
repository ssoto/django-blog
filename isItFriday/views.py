from django.shortcuts import render
from .models import GifDate
from datetime import datetime


DEFAULT_IMAGE = 'http://sd.keepcalm-o-matic.co.uk/i/the-problem-with-today-is-that-its-not-friday.png'
MONTDAY_TO_THURSDAY = 'https://media.giphy.com/media/dBzquitQiuhjO/giphy.gif'
GIFS = {
    # monday
    0: MONTDAY_TO_THURSDAY,
    1: MONTDAY_TO_THURSDAY,
    2: DEFAULT_IMAGE,
    3: DEFAULT_IMAGE,
    # the great friday
    4: 'https://media.giphy.com/media/3oEjHKjVoNVsCeMoDe/giphy.gif',
    # saturday
    5: 'https://media.giphy.com/media/l2R072qHOAH9YceZ2/giphy.gif',
    # sunday
    6: 'https://media.giphy.com/media/3osxYva0ooiSryNiBa/giphy.gif',
}


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
