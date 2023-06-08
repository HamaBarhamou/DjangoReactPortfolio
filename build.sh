#!/usr/bin/env bash

curl -sSL https://install.python-poetry.org | python3 -

set -o errexit  # exit on error

#pip install -r requirements.txt
poetry install

npm install
npm run build

python manage.py collectstatic --no-input
python manage.py migrate