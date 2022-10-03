#!/usr/bin/python3

from datetime import datetime
from fabric.api import local
import os.path as path


def do_pack():
	date = str(datetime.now())
	for i in [':','-','.',' ']:
		date = date.replace(i, '')
	file = f"web_static_{date}.tgz"

	if not path.isdir("versions"):
		local("mkdir versions")
	if local(f"tar -czvf versions/{file} web_static").failed:
		return None

	return file
