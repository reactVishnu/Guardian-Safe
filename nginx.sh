#!/bin/bash

sudo cp -rf app.conf /etc/ngnix/conf.d
chmod 710 /cd /var/lib/jenkins/workspace/Guardian\ Safe\ Ci-CD

sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
sudo ngnix -t

sudo systemctl start ngnix
sudo systemctl status ngnix

echo "Ngnix has been started"

sudo systemctl status gunicorn

