#!/usr/bin/env python
import os,shutil
import subprocess
from subprocess import check_call
import pyfiglet
print("\n ")
def dem():
    result = pyfiglet.figlet_format("Doc Scanner", font = "slant"  )
    print(result)
    print("""
--------------------------------------------------------------------------------------------------------------------------------------------------
(1) Install Tools
(2) Scanning
-------------------------------------------------------------------------------------------------------------------------------------------------
""")
dem()
a=int(input("Select Machine : "))
if a==1:
    print ("\n")
    print ("""
--------------------------------------------------------------------------------------------------------------------------------------------------
(1) Ubuntu                                
(2) Linux                                
--------------------------------------------------------------------------------------------------------------------------------------------------
""")

    
    b=int(input("Select tool to install :"))
    if  b==1:
        cmd=os.system("clear")
        print("""
--------------------------------------------------------------------------------------------------------------------------------------------------
(1) Trivy
(2) Clair
(3) Grype-Anchore
---------------------------------------------------------------------------------------------------------------------------------------------------
""")
        c=int(input("Enter your choice here:"))
        if c==1:
            cmd = os.system("sudo apt-get install wget apt-transport-https gnupg lsb-release && wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -  && echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list && sudo apt-get update && sudo apt-get install trivy")
            dem()
        elif c==2:
            print( " We need \"go 1.16\" for this tool ")
            #cmd =os.system("sudo apt install golang-go")
            os.chdir("..")
            cmd =os.system("sudo git clone https://github.com/quay/clair.git")
            cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
            dem()
            dem()
        elif c==3:
            cmd=os.system("sudo su")
            cmd=os.system("curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin | quit")
    elif b==2:
        cmd=os.system("clear")
        print("""
--------------------------------------------------------------------------------------------------------------------------------------------------
(1) Trivy
(2) Clair
(3) Anchore
---------------------------------------------------------------------------------------------------------------------------------------------------
""")
    d=int(input("Select tool to install:"))
    if d==1:
        cmd = os.system("wget https://github.com/aquasecurity/trivy/releases/download/v0.19.2/trivy_0.19.2_Linux-64bit.deb && sudo dpkg -i trivy_0.19.2_Linux-64bit.deb")
        dem()
    elif d==2:
        print( " We need \"go 1.16\" for this tool ")
        os.chdir("..")
        #cmd =os.system("sudo apt install golang-go")
        cmd =os.system("sudo git clone https://github.com/quay/clair.git ")
        cmd=os.system("cd | GO111MODULE=on go get github.com/quay/clair/v4/cmd/clairctl@latest ")
        dem()
    elif d==3:
        cmd=os.system("sudo su")
        cmd=os.system("curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin | quit")

        
elif a==2:
    print("Select the tool")
            print("""
--------------------------------------------------------------------------------------------------------------------------------------------------
(1) Trivy
(2) Clair
(3) Grype-Anchore
(4) Combined Tools

---------------------------------------------------------------------------------------------------------------------------------------------------
""")
    
    e=int(input("Enter your choice here:"))
    if e==1:
        iname=str(input("Enter image name:"))
        order="trivy image {} > trivy.txt".format(iname)
        cmd=os.system(order)
    if e==2:
        iname=str(input("Enter image name:"))
        
        os.chdir("..")
        os.chdir("clair")
        cmd=os.system(" sudo make local-dev-up-with-quay")
        hpath=os.chdir("..")
        cmd=os.chdir("go/bin")
        order1=" ./clairctl -D report {} > clair.txt".format(iname)
        cmd=os.system(order1)
        bpath=os.getcwd()
        source1=a+"/clair.txt"
        cmd=shutil.move(source1,path)
        os.chdir("..")
        os.chdir("clair")
        cmd=os.system(" sudo make local-dev-down")
        
    if e==3:
        iname=str(input("Enter image name:"))
        #fname=str(input("Enter outputfilename:"))
        order="grype {}  >grype.txt | awk '{print $1}'".format(iname)
        cmd=os.system(order)
        
    if e==4:
        source=os.getcwd()
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
        os.chdir("clair")
        cmd=os.system(" sudo make local-dev-up-with-quay")
        hpath=os.chdir("..")
        cmd=os.chdir("go/bin")
        order1=" ./clairctl -D report {} > clair.txt".format(iname)
        cmd=os.system(order1)
        bpath=os.getcwd()
        source1=a+"/clair.txt"
        cmd=shutil.move(source1,dest)
        os.chdir("..")
        os.chdir("clair")
        cmd=os.system(" sudo make local-dev-down")

        os.chdir(dest)
        cmd=os.system("awk '/CVE/{print $3,$4;}' trivy.txt | sed 's/|/ /g' |sed 's/ //g' > cvet.txt")
        cmd=os.system("awk '/CVE/{print $1}' g.txt | sed 's/ //g'>>cvet.txt")
        cmd=os.system("awk '/CVE/{print $3,$4;}' clair.txt | sed 's/ //g' >> cvet.txt")
        cmd=os.system("sed 's/ //g' cvet.txt")
        cmd=os.system("sort cvet.txt | uniq >final.txt")
        cmd=os.system("sudo rm g.txt")
        
        
        
    
        
        

