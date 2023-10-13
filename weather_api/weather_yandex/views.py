from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from django.conf import settings
from rest_framework.response import Response

from .serializers import WeatherSerializer
from .models import Weather
from .utils import request_weather, create_model, strtoi_minutes


class GetWeather(ListAPIView):
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()

    def get(self, request, *args, **kwargs):
        weather_req = request_weather(self.request.query_params.get("city"), settings.API_KEY)
        try:
            weather_model_latest = Weather.objects.latest('id')
        except Exception:  # if first query fails
            weather_model = create_model(weather_req)
            serializer = WeatherSerializer(weather_model)
            return Response(serializer.data)
        weather_req_time = strtoi_minutes(weather_model_latest.timestamp)
        weather_model_latest_time = strtoi_minutes(weather_req["timestamp"])
        print(abs(weather_req_time - weather_model_latest_time))
        if abs(weather_req_time - weather_model_latest_time) >= 30:
            weather_model = create_model(weather_req)
            serializer = WeatherSerializer(weather_model)
            return Response(serializer.data)
        else:
            weather_model = Weather.objects.latest('id')
            serializer = WeatherSerializer(weather_model)
            return Response(serializer.data)


class GetAll(ListAPIView):    # helper
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
