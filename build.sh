#!/usr/bin/env bash

curl -sSL https://install.python-poetry.org | python3 -
exit


set -o errexit  # exit on error

#pip install -r requirements.txt
poetry shell
poetry install

npm install
npm run build

python manage.py collectstatic --no-input
python manage.py migrate