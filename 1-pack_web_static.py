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
        file = f"web_static_{date}.tgz"
        local("mkdir versions")
        local(f"tar -czvf versions/{file} web_static")
        return file
    except:
        return None