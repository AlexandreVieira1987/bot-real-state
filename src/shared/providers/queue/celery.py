from celery import Celery
from celery.schedules import crontab
import uuid
import os

redis_host = os.environ.get('REDIS_HOST', 'redis://localhost:6379/0')
hour = os.environ.get('SCHEDULE_HOUR', 10)
minutes = os.environ.get('SCHEDULE_MINUTES', 0)

app = Celery('tasks', broker = redis_host, backend = redis_host, concurrency = 2)


@app.on_after_configure.connect
def setup_task(sender, **kwargs):
    sender.add_periodic_task(crontab(minute = minutes, hour = hour), queue_search_links)


@app.task
def queue_search_links():
    from src.modules.search.SearchController import SearchController

    read = SearchController()
    return read.execute()


@app.task
def queue_read_link(link):
    from src.modules.search.useCase.ReadLinkUseCase import ReadLinkUseCase

    read = ReadLinkUseCase()
    return read.execute(link, uuid.uuid4())