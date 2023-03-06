from celery import Celery
import uuid
from src.modules.search.useCase.ReadLinkUseCase import ReadLinkUseCase
import os

redis_host = os.environ.get('REDIS_HOST', 'redis://localhost:6379/0')

app = Celery('tasks', broker = redis_host, backend = redis_host, concurrency = 2)


@app.task
def queue_read_link(link):
    read = ReadLinkUseCase()
    return read.execute(link, uuid.uuid4())