from fabric.api import *
from fabric.colors import green, red, yellow, blue
from fabric.contrib.console import confirm

env.hosts = ["rsj217@localhost"]
env.password = "sirui"
env.user = "rsj217"


def deploy():
    print green("Start to Deploy the Project")
    print green("="*40)
    print blue("create the project directory")
    print blue("*"*40)
    with settings(warn_only=True):
        result =  sudo("mkdir /var/deploy")
    if result.failed:
        sudo("rm -rf /var/deploy/*.*")
    sudo("chown -R rsj217:rsj217 /var/deploy")   
    print blue("get the source code from remote")
    print blue("*"*40)
    with cd("/var/deploy/"):
        with settings(warn_only=True):
            result = run("git clone https://coding.net/rsj217/myproject.git")
        if result.failed:
            run("rm -rf myproject")
            run("git clone https://coding.net/rsj217/myproject.git")

    print blue("install the virtualenv")
    print blue("*"*40)
    sudo("apt-get install python-virtualenv")    
    
    print blue("create the virtual env")    
    print blue("*"*40)
    with cd("/var/deploy"):
        result = run("virtualenv venv")
        run("source venv/bin/activate; pip install -r /var/deploy/myproject/requirements.txt")




# def touch():
#    with settings(warn_only=True):
#        result = sudo("touch /test.txt")  
#    if result.failed and not confirm("Tests faiked"):
#        abort("aborting !!!")


