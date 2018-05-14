from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, shared_task
from django.conf import settings
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryapp.settings')

app = Celery('celeryapp')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))
  print('hello world')


app.conf.beat_schedule = {
    # 'add-every-minute-contrab': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': crontab(),
    #     'args': (16, 16),
    # },
    'add-every-5-seconds': {
        'task': 'vubon',
        'schedule': 5.0,
        # 'args': (16, 16)
    },
    # 'add-every-30-seconds': {
    #     'task': 'sum_two_numbers',
    #     'schedule': 30.0,
    #     'args': (16, 16)
    # },
    # run this cron job every 4 am
    # 'add-every-day-contrab':{
    #     'task': 'task name ',
    #     'schedule': crontab(hour=4, minute=0)
    # },
    # 'add-every-minute-contrab': {
    #     'task': 'data_checking',
    #     'schedule': crontab(),
    # },
}