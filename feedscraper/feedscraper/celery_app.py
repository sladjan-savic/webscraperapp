import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feedscraper.settings')

app = Celery('feedscraper')
app.conf.enable_utc = False
app.conf.update(timezone='CET')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    "Scrape AAPL feeds": {
        "task": "feedsapi.tasks.crawl_aapl_feeds",
        "schedule": 60.0,
    },
    "Scrape TWTR feed": {
        "task": "feedsapi.tasks.crawl_twtr_feeds",
        "schedule": 60.0,
    },
    "Scrape GC_GOLD feed": {
        "task": "feedsapi.tasks.crawl_gc_gold_feeds",
        "schedule": 60.0,
    },
    "Scrape INTC feed": {
        "task": "feedsapi.tasks.crawl_intc_feeds",
        "schedule": 60.0,
    },
}

app.autodiscover_tasks()
