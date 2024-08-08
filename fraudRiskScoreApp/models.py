from django.db import models

# Create your models here.

from django.db import models

class Riskscore(models.Model):
    customerid = models.CharField(max_length=8)
    accountnumber = models.CharField(max_length=8)
    transactiontype = models.CharField(max_length=6)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    accountbalance = models.DecimalField(max_digits=10, decimal_places=2)
    receivername = models.CharField(max_length=100)
    transactiontime = models.DateTimeField()
    riskscore = models.DecimalField(max_digits=5, decimal_places=2)
    transactionid = models.CharField(max_length=100,unique=True,default='00000000')

    class Meta:
        db_table = 'riskscore'
