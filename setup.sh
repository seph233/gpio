#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
deactivate

sudo cp gpio.service /lib/systemd/system/
sudo systemctl enable gpio
sudo systemctl start gpio

sudo cp gpio.nginx /etc/nginx/sites-available/gpio
sudo ln -s /etc/nginx/sites-available/gpio /etc/nginx/sites-enabled/gpio
sudo systemctl restart nginx

