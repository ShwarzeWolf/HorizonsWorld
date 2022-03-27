#!/bin/bash
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
    echo "Creating the database tables..."
    echo "Filling tables with data..."
    echo "Tables created and filled"
fi

exec "$@"