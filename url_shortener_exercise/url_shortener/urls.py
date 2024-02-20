from django.urls import path
from .views import shorten_url, resolve_url

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('<str:short_url>/', resolve_url, name='resolve_url'),
]

