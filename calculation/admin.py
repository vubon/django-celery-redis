from django.contrib import admin
from .models import Balances, GetData, TransferAmount

# Register your models here.

admin.site.register(Balances)
admin.site.register(GetData)
admin.site.register(TransferAmount)
