from django.db import models


class Indicator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
    

class IndicatorValue(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField()
    def __str__(self):
        return f'{self.indicator.name} on {self.date}'