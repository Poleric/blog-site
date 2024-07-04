FROM python:3.12-alpine

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

COPY requirements requirements
RUN pip install --upgrade pip && pip install -r requirements/prod.txt

WORKDIR /app

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
    gunicorn apps.blogsite.wsgi:application
