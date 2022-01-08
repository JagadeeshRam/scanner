#!/usr/bin/env python
import os,shutil
import subprocess
import os.path
from subprocess import check_call
from pyfiglet import Figlet
from termcolor import colored
from simple_colors import *
import psycopg2
import datetime
from database import *
def banner():
     print("""\033[1;32m
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                          █████████  ████                          █████     █████████                                                             
                          ███░░░░░███░░███                         ░░███     ███░░░░░███                                                            
                         ███     ░░░  ░███   ██████  █████ ████  ███████    ░███    ░░░   ██████   ██████   ████████   ████████    ██████  ████████ 
                        ░███          ░███  ███░░███░░███ ░███  ███░░███    ░░█████████  ███░░███ ░░░░░███ ░░███░░███ ░░███░░███  ███░░███░░███░░███
                        ░███          ░███ ░███ ░███ ░███ ░███ ░███ ░███     ░░░░░░░░███░███ ░░░   ███████  ░███ ░███  ░███ ░███ ░███████  ░███ ░░░ 
                        ░░███     ███ ░███ ░███ ░███ ░███ ░███ ░███ ░███     ███    ░███░███  ███ ███░░███  ░███ ░███  ░███ ░███ ░███░░░   ░███     
                         ░░█████████  █████░░██████  ░░████████░░████████   ░░█████████ ░░██████ ░░████████ ████ █████ ████ █████░░██████  █████    
                          ░░░░░░░░░  ░░░░░  ░░░░░░    ░░░░░░░░  ░░░░░░░░     ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░     
                                                                                                                                                    Coded By Jagadeesh Ram Ch
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                  Note: Please give numerical numbers for selection
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
def ubuntu():
    path=os.getcwd()
    os.system("sudo apt update")
    os.system("sudo apt -y upgrade")
    os.system("sudo apt-get install -y libpq-dev")
    os.system(" sudo apt install -y postgresql postgresql-client")
    os.system("clear")
    connection()
    banner()
    print(""" 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                       Machine to install Podman and Go
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                (1) Ubuntu
                                                                                (2) Kali LInux/Debian
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
    d=int(input("Please Select machine:"))
    if d==1:
         os.system("sudo snap install go --classic")
         output = subprocess. getoutput("lsb_release -r | grep Release| awk '{print $2}'")
         os.system("sudo apt-get install curl wget gnupg2 -y")
         order1='echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_{}/ /" | sudo tee  /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list'.format(output)
         os.system(order1)
         order2='curl -L "https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_{}/Release.key" | sudo apt-key add -'.format(output)
         os.system(order2)
         os.system("sudo apt-get update")
         os.system("sudo apt-get -y upgrade")
         os.system("sudo apt-get -y install podman")
            
    if d==2:
         os.system("sudo apt install golang-go")
         os.system("sudo apt-get -y install podman")
    print(""" 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    Tools
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                (1) Trivy
                                                                                (2) Clair
                                                                                (3) Grype-Anchore
                                                                                (4) All Tools
                                                                                (5) Exit
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
    c=int(input("Please Select to tool to install:"))
    if c==1:
        file_path=path+"/trivy_0.22.0_Linux-64bit.deb"
        if os.path.isfile(file_path):
             os.system("sudo rm -r trivy_0.22.0_Linux-64bit.deb")
        else:
             cmd = os.system("wget https://github.com/aquasecurity/trivy/releases/download/v0.22.0/trivy_0.22.0_Linux-64bit.deb && sudo dpkg -i trivy_0.22.0_Linux-64bit.deb")
        os.system("clear")
        
    elif c==2:
        path=os.getcwd()
        
        p=path.split("/")
        p_path=("/"+p[1]+"/"+p[2])
        os.chdir(p_path)
        cmd =os.system("sudo git clone https://github.com/quay/clair.git")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        os.chdir(path)
        os.system("clear")
        
    elif c==3:
        cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")
        os.chdir(path)
        os.system("clear")
        
    elif c==4:
        file_path=path+"/trivy_0.22.0_Linux-64bit.deb"
        if os.path.isfile(file_path):
             os.system("sudo rm -r trivy_0.22.0_Linux-64bit.deb")
        else:
             cmd = os.system("wget https://github.com/aquasecurity/trivy/releases/download/v0.22.0/trivy_0.22.0_Linux-64bit.deb && sudo dpkg -i trivy_0.22.0_Linux-64bit.deb")
        cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")
        path=os.getcwd()
        p=path.split("/")
        p_path=("/"+p[1]+"/"+p[2])
        os.chdir(p_path)
        cmd =os.system("sudo git clone https://github.com/quay/clair.git")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        os.chdir(path)
        os.system("clear")
    elif c==5:
        exit()
        
def centos():
    os.system("sudo yum update")
    os.system("sudo yum -y upgrade")
    os.system("sudo yum install golang-bin")
    #os.system("sudo apt-get install -y libpq-dev")
    os.system("sudo dnf install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm")
    os.system(" sudo dnf -qy module disable postgresql")
    os.system("sudo dnf install postgresql13 postgresql13-server")
    os.system("sudo /usr/pgsql-13/bin/postgresql-13-setup initdb")
    os.system("sudo systemctl enable --now postgresql-13")
    os.system("sudo systemctl start postgresql")
    os.system("clear")
    connection()
    
    
    print(""" 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    Tools
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                (1) Trivy
                                                                                (2) Clair
                                                                                (3) Grype-Anchore
                                                                                (4) All Tools
                                                                                (5) Back
                                                                                (6) Exit
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
    d=int(input(red("Please Select tool to install:",'bold')))
    if d==1:
        cmd = os.system("sudo rpm -ivh https://github.com/aquasecurity/trivy/releases/download/v0.18.3/trivy_0.18.3_Linux-64bit.rpm")
        os.system("clear")
    elif d==2:
        path=os.getcwd()
        p=path.split("/")
        p_path=("/"+p[1]+"/"+p[2])
        os.chdir(p_path)
        os.system("sudo yum -y install podman")
        cmd =os.system("sudo git clone https://github.com/quay/clair.git ")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        os.chdir(path)
        os.system("clear")
    elif d==3:
        cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")
        os.system("clear")
    elif d==4:
        cmd = os.system("sudo rpm -ivh https://github.com/aquasecurity/trivy/releases/download/v0.18.3/trivy_0.18.3_Linux-64bit.rpm")
        cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")
        path=os.getcwd()
        os.system("sudo yum -y install  podman")
        p=path.split("/")
        p_path=("/"+p[1]+"/"+p[2])
        os.chdir(p_path)
        cmd =os.system("sudo git clone https://github.com/quay/clair.git ")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        os.chdir(path)
        os.system("clear")
    elif d==5:
        dem()
    elif d==6:
        exit()
