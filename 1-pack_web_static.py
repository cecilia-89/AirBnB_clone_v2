#!/usr/bin/python3
"""Fabfile to generates a .tgz archive from the contents of web_static.
"""

from time import strftime
from fabric.api import local
import os.path as path


def do_pack():
    """Creates an archive of web_static folder.
    """
    try:
        date = strf("%Y%M%d%H%M%S")
        file = f"web_static_{date}.tgz"
        local("mkdir versions")
        local(f"tar -czvf versions/{file} web_static")
        return file

    except Exception as err:
        return None
