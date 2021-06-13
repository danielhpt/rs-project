FROM python:3.9.2-slim-buster
RUN apt update && apt install -y sqlite3 gcc libpq-dev
WORKDIR /web
ADD . /web
RUN pip install -r requirements.txt
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]