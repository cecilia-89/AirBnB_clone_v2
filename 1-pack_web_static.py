#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.

from time import strftime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
