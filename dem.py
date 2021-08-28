#!/usr/bin/env python
import os
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
a=int(input("Enter your choise here : "))
if a==1:
    print ("\n")
    print ("""
--------------------------------------------------------------------------------------------------------------------------------------------------
(1) Ubuntu                                
(2) Linux                                
--------------------------------------------------------------------------------------------------------------------------------------------------

""")

    
    b=int(input("Enter your choice here :"))
    if  b==1:
        cmd=os.system("clear")
        print("""
--------------------------------------------------------------------------------------------------------------------------------------------------
(1) Trivy
(2) Clair 
---------------------------------------------------------------------------------------------------------------------------------------------------
""")
        c=int(input("Enter your choice here:"))
        if c==1:
            cmd = os.system("sudo apt-get install wget apt-transport-https gnupg lsb-release && wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -  && echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list && sudo apt-get update && sudo apt-get install trivy")
            dem()
        elif c==2:
            print( " We need \"go\" for this tool ")
            cmd =os.system("sudo apt install golang-go")
            cmd =os.system("sudo git clone https://github.com/quay/clair.git && cd clair && sudo  make local-dev-up-with-quay")
            dem()
    elif b==2:
        cmd=os.system("clear")
        print("""
--------------------------------------------------------------------------------------------------------------------------------------------------
(1) Trivy
(2) Clair
(3) Docker    
---------------------------------------------------------------------------------------------------------------------------------------------------
""")
    d=int(input("Enter your choice here:"))
    if d==1:
        cmd = os.system("wget https://github.com/aquasecurity/trivy/releases/download/v0.19.2/trivy_0.19.2_Linux-64bit.deb && sudo dpkg -i trivy_0.19.2_Linux-64bit.deb")
    elif d==2:
        print( " We need \"go\" for this tool ")
        cmd =os.system("sudo apt install golang-go")
        cmd =os.system("sudo git clone https://github.com/quay/clair.git && cd clair && sudo  make local-dev-up-with-quay")
        
        


