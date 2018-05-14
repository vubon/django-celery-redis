from __future__ import absolute_import, unicode_literals
import random
from celery import shared_task

from celeryapp.celery import app
from .models import GetData
from django.db.models import Q, F


# @shared_task(name="sum_two_numbers")
# def add(x, y):
#     return x + y
#
#

@shared_task(name='vubon')
def test():
    print(' Hello world')
    return 'test'

# @shared_task(name="multiply_two_numbers")
# def mul():
#     # total = x * (y * random.randint(3, 100))
#     return '12345668'

#
# @shared_task(name="sum_list_numbers")
# def xsum(numbers):
#     return sum(numbers)


@shared_task(name="data_checking")
def data_add():
    json_data = GetData.objects.get_data_from_db()
    return json_data
