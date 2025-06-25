import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

app.conf.broker_url = os.environ.get('REDIS_URL')
app.conf.result_backend = os.environ.get('REDIS_URL')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'signout-all-visitors-7pm': {
        'task': 'visitor_sign_in.tasks.signout_all_visitors',  # Adjust path to match your app name
        'schedule': crontab(hour=11, minute=20),  # 7:00 PM every day
    },
}
