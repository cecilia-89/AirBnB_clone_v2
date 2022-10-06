#!/usr/bin/python3
"""
Fabric script generates .tgz archive of all in web_static/ using func 'do_pack'
Usage: fab -f 1-pack_web_static.py do_pack
"""
from fabric.api import local
from time import strftime


def do_pack():
    """generate .tgz archive of web_static/ folder"""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        msg = 'Packing web_static to {}'.format(filename)
        print(msg)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None