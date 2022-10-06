#!/usr/bin/python3
"""
Module: 1-pack_web_static
"""
from fabric.api import local
from time import strftime


def do_pack():
    """creates a .tgz archive"""
    date_time = strf("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(date_time)
        msg = 'Packing web_static to {}'.format(filename)
        print(msg)
        local("tar -cvzf {} web_static/".format(filename))
        return filename

    except:
        return None