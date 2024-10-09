FROM python:3.11

RUN mkdir /booking

WORKDIR /booking

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--reload", "--log-level", "debug", "-b", "0.0.0.0:8000", "app.main:app"]

# CMD ["gunicorn", "app.main:app", "--workers", "4", "--workers-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]