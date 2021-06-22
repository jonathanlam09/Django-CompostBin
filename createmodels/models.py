from django.db import models
import datetime as dt

# Create your models here.
class sensors(models.Model):
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Moisturelvl = models.IntegerField()
    DataDate = models.DateTimeField()

    def __str__(self):
        return str(f'{self.Temperature}{self.Humidity}{self.Moisturelvl}{self.DataDate}')

