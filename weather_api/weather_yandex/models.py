from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=255)
    temperature = models.IntegerField()
    pressure = models.IntegerField()
    wind_vel = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.city}: {self.temperature}, {self.pressure}, {self.wind_vel}, {self.timestamp}'
