#!/bin/sh

cd ~/qetela-server
git pull
source /root/env/bin/activate
pip install -r requirements.txt
./manage.py migrate
sudo supervisorctl restart qetela
