#!/bin/bash
echo "Initializing project..."

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres start..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 2
    done

    echo "Postgres started"
fi

if [ "$APP_ENV" = "development" ]
then
    echo "Creating the database, filling tables..."
    FILE=manage.py

    while ! test -f "$FILE" ; do
      echo "waiting for file"
      sleep 1
    done

    python manage.py
    echo "Tables created and filled"
fi

while true; do
  sleep 1;
  done

exec "$@"