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
#from first import *
def dem(path):
    print("""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
									Choose Your Option
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
									(1) Install Tools
									(2) Scanning
									(3) Data Base Reports
									(4) Exit
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")

def trivy(path):
    f_path=path+"/trivy_reports"
    #print(f_path)
    if os.path.isdir(f_path):
        pass
    else:
         os.system("mkdir trivy_reports")
    iname=str(input(red("Enter image name:","bold")))
    fname=str(input(yellow("Enter output file name:","bold")))
    file_path=path+"/trivy_reports"+fname+".txt"
    if os.path.isfile(file_path):
        print("File_name exists")
        fname=str(input("Enter output file name:"))
    else:    
        pass
    order="trivy image {} > {}".format(iname,file_path)
    os.system(order)
    os.system("cat {}".format(file_path))
    print(" The data is stored in the file:",file_path)
    
    
    print("Inserting data to Trivy table")
    try:
        connection = psycopg2.connect(database='scanner', user='scan', password='password', host='127.0.0.1', port= '5432')

        cursor = connection.cursor()
        time= datetime.datetime.now()
        sql_insert_blob_query = """ INSERT INTO Trivy ( file_name, Time_stamp,file) VALUES (%s,%s,%s)"""

        #empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(file_path)
        # Convert data into tuple format
        insert_blob_tuple = (fname, time, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Data and file inserted successfully in Trivy table", result)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Failed inserting data to trivy table {}".format(error))

def clair(path):
 
    #print(path)
    os.chdir(path)
    p=path.split('/')
    p_path="/"+p[1]+"/"+p[2]+"/"
    #print(p_path)
    #print(path)
    file_path=path+"/clair_reports"
    if os.path.isdir(file_path):
        pass
    else:
        os.system("mkdir clair_reports")
        
    a=os.getcwd()
    #print("hh",a)
    c=p_path+"clair"
    b=os.chdir(c)
   
    a=os.getcwd()
    #print("aa:",a)
    cmd=os.system(" sudo make local-dev-up-with-quay")
    os.chdir(path)
    print ("\n")
    print ("""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
									  Select Format of tool 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
										(1) GUI                              
										(2) Command Line
										(3) Back
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    b=int(input(red("Select Format:",'bold')))
    if b==1:
        iname=str(input(red("Enter image name:","bold")))
        tname=str(input(yellow("Enter output file name:","bold")))
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
        #c=os.getcwd()
        cpath=c+"/local-dev/clair/config.yaml"
        #print("bb:",c)
        os.chdir("..") 
        hpath=p_path+"go/bin"
        #print(hpath)
        os.chdir(hpath)
        gpath=os.getcwd()
        #print(gpath)
        #print("aa:",path)
        iname=str(input(red("Enter image name:","bold")))
        fname=str(input(yellow("Enter output file name:","bold")))
        file_path=path+"/clair_reports/"+fname+".txt"
        if os.path.isfile(file_path):
            print("File_name exists")
            fname=str(input("Enter output file name:"))
        else:    
            pass
        order1=" ./clairctl -D  -c {} report {} > {}".format(cpath,iname,file_path)
        cmd=os.system(order1)
        os.system("cat  {}".format(file_path))
        print(" The data is stored in the file:",file_path)
        #print("hh:",path)
        #source1=gpath+"/"+fname
        #scmd=shutil.move(source1,path)
        print(path)
        os.chdir(path)
        try:
            
            connection = psycopg2.connect(database='scanner', user='scan', password='password', host='127.0.0.1', port= '5432')

            cursor = connection.cursor()
            time= datetime.datetime.now()
            sql_insert_blob_query = """ INSERT INTO Clair( file_name, Time_stamp,file) VALUES (%s,%s,%s)"""
            file = convertToBinaryData(file_path)
            insert_blob_tuple = (fname, time, file)
            result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
            connection.commit()
            print("Data and file inserted successfully in Clair table", result)

        except (Exception, psycopg2.DatabaseError) as error:
            
            print("Failed inserting data to Clair table {}".format(error))
        
    if b==3:
        #print(path)
        dem(path)
        
def grype(path):
    
    file_path=path+"/grype_reports/"
    if os.path.isdir(file_path):
        pass
    else:
        os.system("mkdir grype_reports")
    iname=str(input(red("Enter image name:","bold")))
    fname=str(input(yellow("Enter output file name:","bold")))
    file_path=path+"/grype_reports/"+fname+".txt"
    if os.path.isfile(file_path):
        print("File_name exists")
        fname=str(input("Enter output file name:"))
    else:    
        pass
    order="grype {}  >{} ".format(iname,file_path)
    cmd=os.system(order)
    os.system("cat {}".format(file_path))
    print(" The data is stored in the file:",file_path)
    try:
        connection = psycopg2.connect(database='scanner', user='scan', password='password', host='127.0.0.1', port= '5432')
        cursor = connection.cursor()
        time= datetime.datetime.now()
        sql_insert_blob_query = """ INSERT INTO Grype( file_name, Time_stamp,file) VALUES (%s,%s,%s)"""
        file = convertToBinaryData(file_path)
        insert_blob_tuple = (fname, time, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Data and file inserted successfully in grype table", result)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Failed inserting data to grype table {}".format(error))


def combine(path):
    source=os.getcwd()
    #print(source)
    p=path.split('/')
    p_path="/"+p[1]+"/"+p[2]+"/"
    f_path=path+"/combine_reports/"
    #print(p_path)
    
    if os.path.isdir(f_path): 
        os.system("sudo rm -r combine_reports")
    else:
        pass
    cmd=os.system("mkdir combine_reports")
    file_path=path+"/combine_reports/trivy.txt"
    file_path1=path+"/combine_reports/clair.txt"
    file_path2=path+"/combine_reports/grype.txt"
    file_path3=path+"/combine_reports/g.txt"
    dest=os.getcwd()
    time= datetime.datetime.now()
    iname=str(input(yellow("Enter image name:","bold")))
    order="trivy image {} > {}".format(iname,file_path)
    cmd=os.system(order)
    order2="grype {}  >{}".format(iname,file_path2)
    cmd=os.system(order2)
    os.chdir(source)
    order3=" grype {} -o template -t  csv.tmpl >{}".format(iname,file_path3)
    cmd=os.system(order3)
    #cmd=shutil.move(source+"/g.txt",dest)
    c=p_path+"clair"    
    #os.chdir("..")
    #a=os.getcwd()
    os.chdir(c)
    #c=os.getcwd()
    cpath=c+"/local-dev/clair/config.yaml"
    cmd=os.system(" sudo make local-dev-up-with-quay")
    hpath=p_path+"go/bin"
    #print(hpath)
    os.chdir(hpath)
    gpath=os.getcwd()
    #print(gpath)
    order1=" ./clairctl -D -c {} report {} > {}".format(cpath,iname,file_path1)
    cmd=os.system(order1)
    #bpath=os.getcwd()
    #source1=bpath+"/clair.txt"
    #cmd=shutil.move(source1,dest)
    #os.chdir(a)
    os.chdir(c)
    cmd=os.system(" sudo make local-dev-down")
    os.chdir(dest)
    d_path=path+"/combine_reports/"
    os.chdir(d_path)
    cmd=os.system("awk '/CVE/{print $3,$4;}' trivy.txt | sed 's/|/ /g' |sed 's/ //g' > cvet.txt")
    cmd=os.system("awk '/CVE/{print $1}' g.txt | sed 's/ //g'>>cvet.txt")
    cmd=os.system("awk '/CVE/{print $5;}' clair.txt | sed 's/ //g' >> cvet.txt")
    cmd=os.system("sed 's/ //g' cvet.txt >cvett.txt")
    cmd=os.system("sort cvett.txt | uniq >final.txt")
    cmd=os.system("sudo rm g.txt cvet.txt cvett.txt")
    m_path=path+"/combine_reports/final.txt"
    os.system("cat {}".format(m_path))
    print(" The data is stored in the file:",m_path)
    try:
        file_path4=path+"/combine_reports/final.txt"
        connection = psycopg2.connect(database='scanner', user='scan', password='password', host='127.0.0.1', port= '5432')

        cursor = connection.cursor()
        time= datetime.datetime.now()
        post_query = """ INSERT INTO Trivy( file_name, Time_stamp,file) VALUES (%s,%s,%s)"""
        file = convertToBinaryData(file_path)
        insert_blob_tuple = ("trivy", time, file)
        result = cursor.execute(post_query, insert_blob_tuple)
        
        post_query1 = """ INSERT INTO Clair( file_name, Time_stamp,file) VALUES (%s,%s,%s)"""
        file1 = convertToBinaryData(file_path1)
        insert_blob_tuple1 = ("clair", time, file1)
        result = cursor.execute(post_query1, insert_blob_tuple1)
        
        post_query2 = """ INSERT INTO Grype( file_name, Time_stamp,file) VALUES (%s,%s,%s)"""
        file2= convertToBinaryData(file_path2)
        insert_blob_tuple2 = ("grype", time, file2)
        result = cursor.execute(post_query2, insert_blob_tuple2)
        connection.commit()

        post_query3 = """ INSERT INTO Combine( file_name, Time_stamp,file) VALUES (%s,%s,%s)"""
        file3= convertToBinaryData(file_path4)
        insert_blob_tuple3 = ("combine_report", time, file3)
        result = cursor.execute(post_query3, insert_blob_tuple3)
        connection.commit()
        print("Data and file inserted successfully in grype table", result)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Failed inserting data to Combine table {}".format(error))
    os.chdir(path)
    
    
