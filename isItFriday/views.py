from django.shortcuts import render
from datetime import datetime


WEEKDAY_MAPPING = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}


def today(request):
    date_today = datetime.today()
    week_day_name = WEEKDAY_MAPPING.get(date_today.weekday())
    return render(request,
                  'isItFriday/what_day_is_today.html',
                  {'week_day_name': week_day_name})
