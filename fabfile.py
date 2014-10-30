from fabric.api import *
from fabric.colors import green, red, yellow
from fabric.contrib.console import confirm

env.hosts = ["rsj217@localhost"]
env.password = "sirui"

def deploy():
    print green("Start to Deploy the Project")
    print green("="*40)
    with settings(warn_only=True):
        result =  sudo("mkdir /var/deploy")
    if result.failed:
        sudo("rm -rf /var/deploy")
        sudo("mkdir /var/deploy")
    with cd("/var/deploy/"):
        sudo("git clone https://coding.net/rsj217/myproject.git")
    


# from fabric.api import env, run, settings, abort, sudo
# from fabric.contrib.console import confirm


# def config(hosts, password):
#    env.hosts = hosts # ["rsj217@192.168.1.200"]
#    env.password = password #"sirui"

# def touch():
#    with settings(warn_only=True):
#        result = sudo("touch /test.txt")  
#    if result.failed and not confirm("Tests faiked"):
#        abort("aborting !!!")


