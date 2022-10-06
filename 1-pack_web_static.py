#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.

from time import strftime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
	date = strf("%Y%M%d%H%M%S")
	try:
        file = f"web_static_{date}.tgz"
        local("mkdir versions")
        local(f"tar -czvf versions/{file} web_static")
        return file

    except Exception as err:
        return None