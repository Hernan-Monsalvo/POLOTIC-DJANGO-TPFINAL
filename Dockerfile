FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /app

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8000

#esto no funca, tuve que hacer las migraciones desde consola
CMD ["python", "manage.py",  "makemigrations"]
CMD ["python", "manage.py",  "migrate"]

CMD ["python", "manage.py",  "runserver", "0.0.0.0:8000"]
