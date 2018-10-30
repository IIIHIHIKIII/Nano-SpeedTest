from django.db import models

from .account import Account


class Transaction(models.Model):
    origin = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='origin')
    destination = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='destination')
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    amount = models.IntegerField()  # Measured in RAW
    initiated_by = models.GenericIPAddressField(protocol='both')
