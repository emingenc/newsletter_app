FROM tiangolo/uwsgi-nginx-flask:latest


RUN mkdir app

COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt

COPY . app
WORKDIR  /app

