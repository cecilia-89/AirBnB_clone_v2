#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.

from datetime import datetime
from fabric.api import *
import os.path as path

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

    if not path.isdir(archive_path):
        return False

    splited = archive_path.split('.')

    if put(f"{archive_path}, /tmp/").failed:
        return False
    if run(f"tar -xf {archive_path}\
           -C /data/web_static/releases/{splited[0]}").failed:
        return False
    if run(f"rm /tmp/{archive_path}").failed:
        return False
    if run("rm -r /data/web_static/current").failed:
        return False
    if run(f"ln -s /data/web_static/releases/{splited[0]} \
           /data/web_static/current").failed:
        return False
    return True
