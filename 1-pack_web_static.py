#!/usr/bin/python3
"""
Module: 1-pack_web_static
"""
from fabric.api import local
from time import strftime


def do_pack():
    """creates a .tgz archive"""
    date = strf("%Y%M%d%H%M%S")
    try:
		local("mkdir -p versions")
		file = "web_static_{}.tgz".format(date)
        local("tar -czvf versions/{} web_static").format(file)
        return file
    except:
        return None