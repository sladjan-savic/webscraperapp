from time import sleep
from feedscraper.celery_app import app
import feedparser as parser

from .models import Feed
from .remote_urls import aapl_url, twtr_url, gc_fgold__url, intc_url
from .string_literals import AAPL, TWTR, GC_GOLD, INTC


@app.task
def crawl_aapl_feeds():
    print('Crawling aapl rss feeds and creating objects in the database')
    aapl_feed = parser.parse(aapl_url)

    for entry in aapl_feed.entries:
        Feed.objects.create(
            description=entry.description,
            title=entry.title,
            guid=entry.guid,
            link=entry.link,
            published=entry.published,
            tag=AAPL,
        )

        sleep(3)


@app.task
def crawl_twtr_feeds():
    print('Crawling twtr rss feeds and creating objects in the database')
    twtr_feed = parser.parse(twtr_url)

    for entry in twtr_feed.entries:
        Feed.objects.create(
            description=entry.description,
            title=entry.title,
            guid=entry.guid,
            link=entry.link,
            published=entry.published,
            tag=TWTR,
        )

        sleep(3)


@app.task
def crawl_gc_gold_feeds():
    print('Crawling gc gold rss feeds and creating objects in the database')
    gc_gold_feed = parser.parse(gc_fgold__url)

    for entry in gc_gold_feed.entries:
        Feed.objects.create(
            description=entry.description,
            title=entry.title,
            guid=entry.guid,
            link=entry.link,
            published=entry.published,
            tag=GC_GOLD,
        )

        sleep(3)


@app.task
def crawl_intc_feeds():
    print('Crawling intc rss feeds and creating objects in the database')
    intc_feed = parser.parse(intc_url)

    for entry in intc_feed.entries:
        Feed.objects.create(
            description=entry.description,
            title=entry.title,
            guid=entry.guid,
            link=entry.link,
            published=entry.published,
            tag=INTC,
        )

        sleep(3)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
