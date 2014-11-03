# -*- coding: utf-8 -*-

import os
from fabric.api import *
from fabric.colors import green, red, yellow, blue
from fabric.contrib.console import confirm
from fabric.contrib.files import exists

from contextlib import contextmanager

env.hosts = ["rsj217@localhost"]
env.password = "sirui"
env.user = "rsj217"
env.group = "rsj217"

DEPLOY_DIR = '/var/deploy'
PROJECT_DIR = os.path.join(DEPLOY_DIR, 'myproject')
VENV_DIR = os.path.join(DEPLOY_DIR, 'venv')
VENV_PATH = os.path.join(VENV_DIR, 'bin/activate')



def mkdir(prefix=None, path=None):
    mkdir_command = "mkdir {}".format(path)
    if not exists(path):
        if prefix:
            sudo(mkdir_command)
        else:
            run(mkdir_command)

def rm(prefix=None, path=None):
    rm_command = "rm -rf {}".format(path)
    if exists(path):
        if sudo:
            sudo(rm_command)
        else:
            run(rm_command)
    

def deploy():
    print green("Start to Deploy the Project")
    print green("="*40)
    print blue("create the deploy directory")
    print blue("*"*40)

    # 创建部署文件夹
    mkdir('sudo', path=DEPLOY_DIR)    

    # 更改文件夹所属关系    
    sudo("chown -R {}:{} {}".format(env.user, env.group, DEPLOY_DIR))
    print blue("get the source code from remote")
    print blue("*"*40)
    # 获取源代码
    with cd(DEPLOY_DIR):
        with settings(warn_only=True):
            rm(path=PROJECT_DIR,)
        run("git clone https://coding.net/rsj217/myproject.git")

    print blue("install the virtualenv")
    print blue("*"*40)
    # 安装 python 虚拟环境
    sudo("apt-get install python-virtualenv")    
    
    print blue("create the virtual env")    
    print blue("*"*40)
    # 安装 python 第三方库
    with cd(DEPLOY_DIR):
        run("virtualenv {}".format(VENV_DIR))
        with prefix("source {}".format(VENV_PATH)):
            run("pip list")





