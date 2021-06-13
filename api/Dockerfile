FROM python:3.9.2-slim-buster
RUN apt update && apt install -y sqlite3 gcc libpq-dev
WORKDIR /api
ADD . /api
RUN pip install -r requirements.txt
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "run.sh"]