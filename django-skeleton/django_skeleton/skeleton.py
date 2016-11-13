import os
import imp
import shutil
import subprocess


def is_django_installed():
    try:
        imp.find_module('django')
    except ImportError:
        return False
    else:
        return True


def create_project(project_name):
    if not is_django_installed():
        raise ImportError("Django not installed")

    current_dir = os.getcwd()
    cmd = ' '.join(['django-admin', 'startproject', 'website'])
    subprocess.call(cmd, shell=True)
    old_project_name = os.path.join(current_dir, 'website')

    new_project_name = os.path.join(current_dir, project_name)
    os.rename(old_project_name, new_project_name)

    dirs = ['apps', 'docs', 'templates', 'static', 'tests']
    for _dir in dirs:
        path = os.path.join(new_project_name, _dir)
        os.mkdir(path)

    files = ['README.md', 'README.rst', 'apps/__init__.py']
    for _file in files:
        path = os.path.join(new_project_name, _file)
        os.mknod(path)


def create_app(app_name):
    if not is_django_installed():
        raise ImportError("Django not installed")

    current_dir = os.getcwd()
    cmd = ' '.join(['django-admin', 'startapp', app_name])
    subprocess.call(cmd, shell=True)

    old_app_name = os.path.join(current_dir, app_name)
    new_app_name = os.path.join(current_dir, 'apps', app_name)
    shutil.move(old_app_name, new_app_name)
