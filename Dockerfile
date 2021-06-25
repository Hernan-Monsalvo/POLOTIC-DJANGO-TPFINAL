FROM python:3

RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]
EXPOSE 8000

EXPOSE 8000

#esto no funca, tuve que hacer las migraciones desde consola
CMD ["python", "manage.py",  "makemigrations"]
CMD ["python", "manage.py",  "migrate"]

CMD ["python", "manage.py",  "runserver", "0.0.0.0:8000"]
