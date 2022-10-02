#!/usr/bin/env bash
#sets up web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/

echo "Holberton School" | sudo tee -a /data/web_static/releases/test/index.html

sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo sed -i '47a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart
