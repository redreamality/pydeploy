# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.colors import green, red, yellow, blue
from fabric.contrib.console import confirm



env.hosts = ["rsj217@localhost"]
env.password = "sirui"
env.user = "rsj217"
env.group = "rsj217"


def deploy():
    print green("Start to Deploy the Project")
    print green("="*40)
    print blue("create the project directory")
    print blue("*"*40)
    # 创建部署文件夹
    with settings(warn_only=True):
        sudo("mkdir /var/deploy")
        sudo("mkdir /var/deploy/log")
    # 更改文件夹所属关系    
    sudo("chown -R {}:{} /var/deploy".format(env.user, env.group))
    print blue("get the source code from remote")
    print blue("*"*40)
    # 获取源代码
    with cd("/var/deploy/"):
        with settings(warn_only=True):
            result = run("rm -rf myproject")
        run("git clone https://coding.net/rsj217/myproject.git")

    print blue("install the virtualenv")
    print blue("*"*40)
    # 安装 python 虚拟环境
    sudo("apt-get install python-virtualenv")    
    
    print blue("create the virtual env")    
    print blue("*"*40)
    # 安装 python 第三方库
    with cd("/var/deploy"):
        result = run("virtualenv venv")
        run("source venv/bin/activate; pip install -r /var/deploy/myproject/requirements.txt")






