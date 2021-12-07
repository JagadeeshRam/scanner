#!/usr/bin/env python
import os,shutil
import subprocess
import os.path
from subprocess import check_call
from pyfiglet import Figlet
from termcolor import colored
def dem():
    print("""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
									Choose Your Option
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
									(1) Install Tools
									(2) Scanning
									(3) Exit
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
    
def ubuntu():
    os.system("sudo apt update")
    os.system("sudo apt -y upgrade")
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
    c=int(input("Enter your choice here:"))
    if c==1:
        cmd = os.system("sudo apt-get install wget apt-transport-https gnupg lsb-release && wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -  && echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list && sudo apt-get update && sudo apt-get install trivy")
        os.system("clear")
    elif c==2:
        path=os.getcwd()
        print( " We need \"go 1.16\" for this tool ")
        output = subprocess. getoutput("lsb_release -r | grep Release| awk '{print $2}'")
        os.system("sudo apt-get install curl wget gnupg2 -y")
        order1='echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_{}/ /" | sudo tee  /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list'.format(output)
        os.system(order1)
        order2='curl -L "https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_{}/Release.key" | sudo apt-key add -'.format(output)
        os.system(order2)
        os.system("sudo apt-get update")
        os.system("sudo apt-get -y upgrade")
        os.system("sudo apt-get -y install podman")
            #cmd =os.system("sudo apt install golang-go")
        os.chdir("..")
        cmd =os.system("sudo git clone https://github.com/quay/clair.git")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        os.chdir(path)
        os.system("clear")
    elif c==3:
        cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")
        os.system("clear")
    elif c==4:
        cmd = os.system("sudo apt-get install wget apt-transport-https gnupg lsb-release && wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -  && echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list && sudo apt-get update && sudo apt-get install trivy")
        cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")
        path=os.getcwd()
        print( " We need \"go 1.16\" for this tool ")
        output = subprocess. getoutput("lsb_release -r | grep Release| awk '{print $2}'")
        order1='echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_{}/ /" | sudo tee  /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list'.format(output)
        os.system(order1)
        order2='curl -L "https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_{}/Release.key" | sudo apt-key add -'.format(output)
        os.system(order2)
        os.system("sudo apt-get update")
        os.system("sudo apt-get -y upgrade")
        os.system("sudo apt-get -y install podman")
            #cmd =os.system("sudo apt install golang-go")
        os.chdir("..")
        cmd =os.system("sudo git clone https://github.com/quay/clair.git")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        os.chdir(path)

    elif c==5:
        exit()
        
def debian():
    
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
    d=int(input("Select tool to install:"))
    if d==1:
        cmd = os.system("wget https://github.com/aquasecurity/trivy/releases/download/v0.19.2/trivy_0.19.2_Linux-64bit.deb && sudo dpkg -i trivy_0.19.2_Linux-64bit.deb")
        os.system("clear")
    elif d==2:
        print( " We need \"go 1.16\" for this tool ")
        path=os.getcwd()
        os.system("sudo apt-get install -y podman")
        os.chdir("..")
        #cmd =os.system("sudo apt install golang-go")
        cmd =os.system("sudo git clone https://github.com/quay/clair.git ")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        os.chdir(path)
        os.system("clear")
    elif d==3:
        cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")
        os.system("clear")
    elif d==4:
        cmd = os.system("wget https://github.com/aquasecurity/trivy/releases/download/v0.19.2/trivy_0.19.2_Linux-64bit.deb && sudo dpkg -i trivy_0.19.2_Linux-64bit.deb")
        cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")
        path=os.getcwd()
        os.system("sudo apt-get install -y podman")
        print( " We need \"go 1.16\" for this tool ")
        
            #cmd =os.system("sudo apt install golang-go")
        os.chdir("..")
        cmd =os.system("sudo git clone https://github.com/quay/clair.git")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        os.chdir(path)
    elif d==5:
        exit()
                    
def trivy():
    iname=str(input("Enter image name:"))
    fname=str(input("Enter output file name:"))
    if os.path.isfile(fname):
        print("File_name exists")
        fname=str(input("Enter output file name:"))
    else:    
        pass
    order="trivy image {} > {}".format(iname,fname)
    cmd=os.system(order)

def clair(path):
    a=os.getcwd()
    print("hh",a)
    os.chdir(path)
    os.chdir("..")
    bb=os.getcwd()
    print("kk",bb)
    os.chdir("clair")
    a=os.getcwd()
    print("aa:",a)
    cmd=os.system(" sudo make local-dev-up-with-quay")
    print ("\n")
    print ("""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
									  Select Format of tool 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
										(1) GUI                              
										(2) Command Line
										(3) Back
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    b=int(input("Select Format:"))
    if b==1:
        iname=str(input("Enter image name:"))
        tname=str(input("Enter channel name:"))
        rname=str(input("Enter resp name:"))
        order="podman pull {}".format(iname)
        order1="podman login --tls-verify=false localhost:8080 "
        order2="podman tag {} localhost:8080/{}/{}".format(iname,tname,rname)
        order3="podman push --tls-verify=false localhost:8080/{}/{}".format(tname,rname)
        os.system(order)
        os.system(order1)
        os.system(order2)
        os.system(order3)
    
    if b==2:
        c=os.getcwd()
        cpath=c+"/local-dev/clair/config.yaml"
        print("bb:",c)
        hpath=os.chdir("..")
        os.chdir("go/bin")
        gpath=os.getcwd()
        print(gpath)
        iname=str(input("Enter image name:"))
        fname=str(input("Enter output file name:"))
        if os.path.isfile(fname):
            print("File_name exists")
            fname=str(input("Enter output file name:"))
        else:    
            pass
        order1=" ./clairctl -D  -c {} report {} > {}".format(cpath,iname,fname)
        cmd=os.system(order1)
        source1=gpath+"/"+fname
        scmd=shutil.move(source1,path)
        os.chdir(path)
        
    if b==3:
        dem()
        
def grype():
    iname=str(input("Enter image name:"))
    fname=str(input("Enter output file name:"))
    if os.path.isfile(fname):
        print("File_name exists")
        fname=str(input("Enter output file name:"))
    else:    
        pass
    order="grype {}  >{} ".format(iname,fname)
    cmd=os.system(order)
def combine(path):
    source=os.getcwd()
    print(source)
    if os.path.isdir('reports'): 
        os.system("sudo rm -r reports")
    else:
        pass
    cmd=os.system("mkdir reports")
    os.chdir("reports")
    dest=os.getcwd()
    iname=str(input("Enter image name:"))
    order="trivy image {} > trivy.txt".format(iname)
    cmd=os.system(order)
    order2="grype {}  >grype.txt".format(iname)
    cmd=os.system(order2)
    os.chdir(source)
    order3=" grype {} -o template -t  csv.tmpl >g.txt".format(iname)
    cmd=os.system(order3)
    cmd=shutil.move(source+"/g.txt",dest)
        
    os.chdir("..")
    a=os.getcwd()
    os.chdir("clair")
    c=os.getcwd()
    cpath=c+"/local-dev/clair/config.yaml"
    cmd=os.system(" sudo make local-dev-up-with-quay")
    hpath=os.chdir("..")
    cmd=os.chdir("go/bin")
    order1=" ./clairctl -D -c {} report {} > clair.txt".format(cpath,iname)
    cmd=os.system(order1)
    bpath=os.getcwd()
    source1=bpath+"/clair.txt"
    cmd=shutil.move(source1,dest)
    os.chdir(a)
    os.chdir("clair")
    cmd=os.system(" sudo make local-dev-down")
    os.chdir(dest)
    cmd=os.system("awk '/CVE/{print $3,$4;}' trivy.txt | sed 's/|/ /g' |sed 's/ //g' > cvet.txt")
    cmd=os.system("awk '/CVE/{print $1}' g.txt | sed 's/ //g'>>cvet.txt")
    cmd=os.system("awk '/CVE/{print $5;}' clair.txt | sed 's/ //g' >> cvet.txt")
    cmd=os.system("sed 's/ //g' cvet.txt >cvett.txt")
    cmd=os.system("sort cvett.txt | uniq >final.txt")
    cmd=os.system("sudo rm g.txt cvet.txt cvett.txt")
    os.chdir(path)
    
    


while True:
    
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
""")
    print("\n ")
    dem()
    path=os.getcwd()
    a=int(input("Select your option : "))
    if a==1:
        
        print ("\n")
        print ("""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
									  Select Your Machine
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
										(1) Ubuntu                                
										(2) Debian
										(3) Exit
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
        b=int(input("Select Machine:"))
        if  b==1:
            ubuntu()
        if  b==2:
            debian()
        if  b==3:
            exit()
    if a==2:
        os.chdir(path)
        os.system(" sudo systemctl start docker")
        print(path)
        print(""" 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    Tools
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                (1) Trivy
                                                                                (2) Clair
                                                                                (3) Grype-Anchore
                                                                                (4) Combined Tools
                                                                                (5) Back to first
                                                                                (6) Exit
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                        Note:  The reports are stored in text file with tool name as file_name,but for combined tools it was stored in reports folder
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
        e=int(input("Select Tool to scan:"))
        if e==1:
            trivy(path)
        if e==2:
            clair(path)
        if e==3:
            grype(path)
        if e==4:
            combine(path)
        if e==5:
            dem()
        if e==6:
            exit()
        
    if a==3:
        exit()
