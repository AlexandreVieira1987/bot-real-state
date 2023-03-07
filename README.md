# Bot Real State

This project search by grounds in real estate stores of Araranguá city in Santa Catarina State

### Running Locally  (tested only ububtu distro)

1 - Create file .env and define values (use .env.example)

2 - create virtual env

```bash
python -m venv venv
```

3 - active virtual env

```bash
source keyword/bin/activate
```

4 - Install packages

```bas
pip install -r requirements.txt
```

5 Run

```bash
celery -A src.shared.providers.queue worker -l info -c 2 --beat --without-heartbeat
```

### Running in Docker

1 - Create file .env and define values (use .env.example)

2 -  Run docker-compose

```bash
docker-compose up --build
```
