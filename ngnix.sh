#!/bin/bash

sudo cp -rf app.conf /etc/ngnix/conf.d
chmod 710 /var/lib/jenkins/workspace/django-cicd

sudo ngnix -t

sudo systemctl start ngnix
sudo systemctl status ngnix

echo "Ngnix has been started"

sudo systemctl status gunicorn

