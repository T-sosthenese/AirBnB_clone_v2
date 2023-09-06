#!/usr/bin/python3
'''
Distributes the already created archive to remote servers.
'''

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['100.24.242.155', '52.86.39.45']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
        cur_time = datetime.now()
        output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            cur_time.year,
            cur_time.month,
            cur_time.day,
            cur_time.hour,
            cur_time.minute,
            cur_time.second
        )
        try:
            print("Packing web_static to {}".format(output))
            local("tar -cvzf {} web_static".format(output))
            archive_size = os.stat(output).st_size
            print("web_static packed: {} -> {} Bytes".format(
                output, archive_size))
        except Exception:
            output = None
        return output


def do_deploy(archive_path):
    """
    Deploys static files to host servers.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
