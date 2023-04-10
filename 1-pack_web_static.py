#!/usr/bin/python3
""" a python script that generates .tgz
"""
from fabric.operations import local
from datatime import datetime as d


def do_pack():
    """ generates .tgz archive """
    files = "/version/web_static_" + str(d.now().year) + str(d.now().month)
    files += str(d.now().day) + str(d.now().hour) + str(d.now().minute)
    files += str(d.now.second) + ".tgz"
    response = local("mkdir -p versions; tar -cvzf \"%s\" web_static" % files)
    if response.failed:
        return None
    else:
        return files
