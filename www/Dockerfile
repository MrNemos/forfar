FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ADD requirements.txt /
RUN pip install -U pip && pip install -r requirements.txt
WORKDIR /srv/site
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
