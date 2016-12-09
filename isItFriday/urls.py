from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.today),
    url('^days', include('rest_framework.urls')),
]
