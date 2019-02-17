#!/bin/sh

ssh root@68.183.166.133 <<EOF
  cd qetela-server
  git pull
  source /root/env/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  sudo supervisorctl restart qetela
  exit
EOF
