from django.db import models

class Trains(models.Model):
    ordNumber = models.IntegerField(primary_key=True)
    carNumber = models.IntegerField()
    trainIndex = models.IntegerField()
    trainNumber = models.IntegerField()
    carStatus = models.CharField(max_length=40)
    invoiceId = models.IntegerField()
    invoiceNumber = models.CharField(max_length=8)
    stateId = models.IntegerField()
    lastOperDt = models.DateTimeField(max_length=10)