from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import GetData


@shared_task(name='vubon')
def test():
    print(' Hello world')
    return 'test'


@shared_task(name="data_checking")
def data_add():
    json_data = GetData.objects.get_data_from_db()
    return json_data
