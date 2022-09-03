from django.db import models


class GoogleSheet(models.Model):
    order = models.IntegerField()
    usd_price = models.IntegerField()
    rub_price = models.FloatField()
    delivery_time = models.DateField()
    notify = models.BooleanField(default=False)
