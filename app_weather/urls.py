# urls.py in app_weather

from django.urls import path
from .views import current_weather, weather_view

urlpatterns = [
    path('', weather_view),
]