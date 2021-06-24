FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /app

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "TP_POLOTIC", "TP_POLOTIC.wsgi:application"]

