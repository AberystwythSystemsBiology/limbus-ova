#!/bin/bash

docker-compose -f ~/limbus/docker-compose.staging.yml run web sh -c 'yarn install'
docker-compose -f ~/limbus/docker-compose.staging.yml run web sh -c 'yarn install'

if [ ! -d ~/limbus/services/web/migrations/versions ]; then
        mkdir -p ~/limbus/services/web/migrations/versions
    fi

docker-compose -f ~/limbus/docker-compose.staging.yml run web sh -c "alembic revision --autogenerate -m 'Generating database'; alembic upgrade head"

docker-compose -f ~/limbus/docker-compose.staging.yml run web sh -c "flask cmd_setup create-kryten"