from celery import Celery
import uuid
from src.modules.search.useCase.ReadLinkUseCase import ReadLinkUseCase

app = Celery('tasks', broker = 'redis://localhost:6379', backend = 'redis://localhost:6379', concurrency = 2)


@app.task
def queue_read_link(link):
    read = ReadLinkUseCase()
    return read.execute(link, uuid.uuid4())