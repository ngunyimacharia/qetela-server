#!/bin/sh

export DJANGO_SETTINGS_MODULE=qetela.settings.dev
virtualenv -p python3 qetelaenv
source qetelaenv
pip3 install -r requirements.txt
python3 manage.py jenkins --enable-coverage
