from django.urls import path

from .views import GetWeather, GetAll

urlpatterns = [
    path('weather/', GetWeather.as_view()),
    path('weather-all/', GetAll.as_view()),
]
