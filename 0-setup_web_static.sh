#!/usr/bin/env bash
#sets up web servers for the deployment of web_static

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/

echo "Holberton School" > /data/web_static/releases/test/index.html

ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/

sed -i '47a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

service nginx restart

 try:

        

    except Exception as err:
        return None
