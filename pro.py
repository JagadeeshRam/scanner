#!/usr/bin/env python
import os,shutil
import subprocess
from subprocess import check_call
import pyfiglet
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
        print( " We need \"go 1.16\" for this tool ")
            #cmd =os.system("sudo apt install golang-go")
        os.chdir("..")
        cmd =os.system("sudo git clone https://github.com/quay/clair.git")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")

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
         path=os.getcwd()
         cmd = os.system("wget https://github.com/aquasecurity/trivy/releases/download/v0.19.2/trivy_0.19.2_Linux-64bit.deb && sudo dpkg -i trivy_0.19.2_Linux-64bit.deb")
         print( " We need \"go 1.16\" for this tool ")
            #cmd =os.system("sudo apt install golang-go")
         os.chdir("..")
         cmd =os.system("sudo git clone https://github.com/quay/clair.git")
         cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
         os.chdir(path)
         cmd=os.system("sudo curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin ")
    elif d==5:
        exit()
                    
def trivy():
    iname=str(input("Enter image name:"))
    order="trivy image {} > trivy.txt".format(iname)
    cmd=os.system(order)
def clair():
    try:
        path=os.getcwd()
        os.chdir("..")
        os.chdir("clair")
        cmd=os.system(" sudo make local-dev-up-with-quay")
        hpath=os.chdir("..")
        os.chdir("go/bin")
        gpath=os.getcwd()
        iname=str(input("Enter image name:"))
        order1=" ./clairctl -D report {} > clair.txt".format(iname)
        cmd=os.system(order1)
        source1=gpath+"/clair.txt"
        cmd=shutil.move(source1,path)
    except:
        os.chdir("..")
        os.chdir("clair")
        cmd=os.system("sudo systemctl start docker")
        cmd=os.system("sudo docker-compose up -d indexer-quay")
        
def grype():
    iname=str(input("Enter image name:"))
    order="grype {}  >grype.txt | awk '{print $1}'".format(iname)
    cmd=os.system(order)
def combine():
    source=os.getcwd()
    print(source)
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
    try:
        
        a=os.chdir("..")
        print(a)
        os.chdir("clair")
        cmd=os.system(" sudo make local-dev-up-with-quay")
        hpath=os.chdir("..")
        cmd=os.chdir("go/bin")
        order1=" ./clairctl -D report {} > clair.txt".format(iname)
        cmd=os.system(order1)
        bpath=os.getcwd()
        source1=bpath+"/clair.txt"
        cmd=shutil.move(source1,dest)
        os.chdir(a)
        os.chdir("clair")
        cmd=os.system(" sudo make local-dev-down")
    except:
        os.chdir("..")
        os.chdir("clair")
        cmd=os.system("sudo systemctl start docker")
        cmd=os.system("sudo docker-compose up -d indexer-quay")

    os.chdir(dest)
    cmd=os.system("awk '/CVE/{print $3,$4;}' trivy.txt | sed 's/|/ /g' |sed 's/ //g' > cvet.txt")
    cmd=os.system("awk '/CVE/{print $1}' g.txt | sed 's/ //g'>>cvet.txt")
    cmd=os.system("awk '/CVE/{print $3,$4;}' clair.txt | sed 's/ //g' >> cvet.txt")
    cmd=os.system("sed 's/ //g' cvet.txt")
    cmd=os.system("sort cvet.txt | uniq >final.txt")
    cmd=os.system("sudo rm g.txt")
    
    


while True:
    result = pyfiglet.figlet_format("Cloud  Scanner", font = "slant"  )
    print(result)
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
        print(""" 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    Tools
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                (1) Trivy
                                                                                (2) Clair
                                                                                (3) Grype-Anchore
                                                                                (4) Combined Tools
                                                                                (5) Exit
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                        Note:  The reports are stored in text file with tool name as file_name,but for combined tools it was stored in reports folder
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
        e=int(input("Select Tool to scan:"))
        if e==1:
            trivy()
        if e==2:
            clair()
        if e==3:
            grype()
        if e==4:
            combine()
        if e==4:
            exit()
        
    if a==3:
        exit()
