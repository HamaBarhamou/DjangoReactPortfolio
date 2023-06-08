#!/usr/bin/env bash

set -o errexit  # exit on error

#pip install -r requirements.txt
echo "Insatllation des dependance"
poetry --version
poetry install

npm install
npm run build

python manage.py collectstatic --no-input
python manage.py migrate