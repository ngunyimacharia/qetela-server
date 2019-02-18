#!/bin/bash

cd /root/qetela-server
git pull
source /root/env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo supervisorctl restart qetela
