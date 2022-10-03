#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.

from datetime import datetime
from fabric.api import *
import os.path as path

env.user = 'ubuntu'
env.hosts = ['34.225.194.161', '44.197.209.34']


def do_pack():
    """Creates an archive of web_static folder."""
    date = str(datetime.now())
    for i in [':', '-', '.', ' ']:
        date = date.replace(i, '')
    file = f"web_static_{date}.tgz"

    if not path.isdir("versions"):
        local("mkdir versions")
    if local(f"tar -czvf versions/{file} web_static").failed:
        return None

    return file


def do_deploy(archive_path):
    """deploys archive to the remote servers"""

    try:
        path.exists(archive_path)
        splited = archive_path.split('.')[0].split('/')

        put(f'versions/{splited[1]}.tgz', '/tmp/')
        run(f"mkdir -p /data/web_static/releases/{splited[1]}")
        run(f"tar -xf /tmp/{splited[1]}.tgz\
            -C /data/web_static/releases/{splited[1]}")
        run(f"rm /tmp/{splited[1]}.tgz")
        run("rm -r /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{splited[1]} \
            /data/web_static/current")

        return True

    except Exception as err:
        return False
