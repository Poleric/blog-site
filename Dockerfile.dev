FROM python:3.12-alpine

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

WORKDIR /app

COPY requirements requirements
RUN pip install -r requirements/prod.txt

COPY . .

RUN python manage.py collectstatic --noinput --clear

RUN if [ "$DJANGO_SUPERUSER_USERNAME" ]; then \
        python manage.py createsuperuser \
            --noinput \
            --username $DJANGO_SUPERUSER_USERNAME \
            --email $DJANGO_SUPERUSER_EMAIL; \
    fi

CMD set -xe; \
    python manage.py migrate --noinput; \
    gunicorn blogsite.wsgi:application
