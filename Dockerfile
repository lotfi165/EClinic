FROM python:3.12.1-alpine

WORKDIR /usr/src/app

COPY . .

RUN python -m venv venv

RUN source ./venv/bin/activate
RUN pip install -r requirements.txt

WORKDIR /usr/src/app/src

RUN python manage.py collectstatic

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "EClinic.wsgi:application" ]