FROM python:3.9.0

WORKDIR /home/

RUN echo 'lksmaoidmf'

RUN git clone https://github.com/Oh-June-Sang/GIS_2ban_2.git

WORKDIR /home/GIS_2ban_2

RUN echo "SECRET_KEY=django-insecure-fdpek%5u038xqq(b)ty2f-r)wtp1x!b7p17v^51lwqz&a=1o%*">.env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash","c","python manage.py collectstatic --noinput --settings=GIS_OH.settings.deploy &&python manage.py migrate --settings=GIS_OH.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=GIS_OH.settings.deploy GIS_OH.wsgi --bind 0.0.0.0:8000"]

