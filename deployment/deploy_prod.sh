#!/bin/sh

cd /root/qetela-server
git pull
source /root/env/bin/activate
pip install -r requirements.txt
./manage.py migrate
python manage.py collectstatic --noinput
sudo supervisorctl restart qetela
