from django.db import models
from django.db.models import Q
from django.utils import timezone
import datetime

# Create your models here.


class GetDataManager(models.Manager):

    @staticmethod
    def check_balance(identify):
        current_bal = Balances.objects.get(identify=identify).amount
        return current_bal

    def get_data_from_db(self):
        get_data = self.filter(Q(is_disabled=False))

        for data in get_data:
            account = data.identify
            current_bal = self.check_balance(account)
            if float(data.amount) <= float(current_bal):
                TransferAmount.objects.create(
                    identify=data.identify,
                    amount=data.amount,
                    timestamp=timezone.now()
                )
                get_update_table = self.filter(pk=data.id)
                next_date = datetime.datetime.now() + datetime.timedelta(days=30)
                get_update_table.update(
                    last_payment=timezone.now(),
                    next_payment=next_date
                )
                balance_table = Balances.objects.filter(identify=data.identify)
               # balance_table_update = balance_table.pk
                new_amount = float(current_bal) - float(data.amount)
                balance_table.update(
                    amount=new_amount
                )
            elif float(data.amount) > float(current_bal):
                message = {"message": "You have no balance.", "status": 400}
                return message
            else:
                continue

        message = {"message": "Task has been completed."}
        return message


class Balances(models.Model):
    identify = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=14, decimal_places=4)

    def __str__(self):
        return self.identify


class GetData(models.Model):
    identify = models.CharField(max_length=20)
    is_disabled = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=14, decimal_places=4)
    last_payment = models.DateTimeField(null=True, blank=True)
    next_payment = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField()

    objects = GetDataManager()

    def __str__(self):
        return self.identify


class TransferAmount(models.Model):
    identify = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=14, decimal_places=4)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.identify
