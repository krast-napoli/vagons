from django.db import models

class Trains(models.Model):
    ordNumber = models.IntegerField(primary_key=True)
    carNumber = models.IntegerField(null=True, blank=True)
    trainIndex = models.IntegerField(null=True, blank=True)
    trainNumber = models.IntegerField(null=True, blank=True)
    carStatus = models.CharField(max_length=40)
    invoiceId = models.IntegerField(null=True, blank=True)
    invoiceNumber = models.CharField(max_length=8)
    stateId = models.IntegerField(null=True, blank=True)
    lastOperDt = models.DateTimeField(max_length=10, null=True, blank=True)