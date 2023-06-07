#!/usr/bin/env bash
sudo apt install gunicorn

set -o errexit  # exit on error

pip install -r requirements.txt

npm install
npm run build

python manage.py collectstatic --no-input
python manage.py migrate