#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['35.153.78.102', '54.160.91.90']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        print("Archive path does not exist: {}\n".format(archive_path))
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"

        print("Uploading the archive to the /tmp/ directory of the web server...\n")
        put(archive_path, '/tmp/')

        print("Creating release directory /data/web_static/releases/{}...\n".format(no_ext))
        run('mkdir -p {}{}/'.format(path, no_ext))

        print("Uncompressing the archive to the release directory...\n")
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))

        print("Deleting the archive from the /tmp/ directory...\n")
        run('rm /tmp/{}'.format(file_n))

        print("Moving contents out of the web_static folder to the release directory...\n")
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        print("Deleting the old symbolic link /data/web_static/current...\n")
        run('rm -rf /data/web_static/current')

        print("Creating a new symbolic link /data/web_static/current linked to the new release...\n")
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        print("Deployment successful!\n")
        return True
    except Exception as e:
        print("Deployment failed: {}\n".format(e))
        return False
