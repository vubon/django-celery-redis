# Django Celery Redis 
This is a basic example scheduler tasks of Django , Celery with Redis 

## You need to install Celery and Redis in your virtual environments 
```bash
pip install celery 
```
and 
```bash
pip install redis 
``` 

## Redis is a broker server 
Also you need to install Redis in your machine 
More details about redis [Redis](https://redis.io/)

### Insert bellow settings in your settings.py 

```python
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

```

## Run your broker server 
```bash
redis-server
```

## Next run your Django server
```bash
python manage.py runserver
``` 

## Next step run your Celery worker 
```bash
celery -A project_name worker -l info

example:

celery -A celearyapp worker -l info
```
you will get task list in your console 

## next run your scheduler 
```bash
celery -A project_name beat -l info

Example:
celery -A celeryapp beat -l info
```
Basically beat will call celery.py and search this his configurations I mean below code block
```python

app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'vubon',
        'schedule': 5.0,
    },
    'add-every-minute-contrab': {
        'task': 'data_checking',
        'schedule': crontab(minute=1),
    },
}
``` 
first one run every 5 seconds and second one run every 1 minute . 

In your celery worker will get information what after running all commands . 

By the way I added a sample app .. It was nothing .. Just query and create three class and one manager for get Data 
You can skip this app. 
