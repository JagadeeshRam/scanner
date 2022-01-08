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

def drop(path):
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

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def retrive(path):

    print("Reading data from  database")
    os.chdir(path)
    #print(path)
    p=path+"/db_reports"
    if os.path.isdir(p):
        pass
    else:
        os.system("mkdir db_reports")
    p1=path+"/db_reports/Trivy"
    p2=path+"/db_reports/clair"
    p3=path+"/db_reports/grype"
    p4=path+"/db_reports/combine"
    if os.path.isdir(p1 and p2 and p3 and p4):
        pass
    else:
        
        os.chdir("db_reports")
        os.system("mkdir Trivy ")
        os.system("mkdir clair")
        os.system("mkdir grype")
        os.system("mkdir combine")
    
    
   
    os.chdir("..")
    drop(path)
    
   
    ID=int(input("Please select your tool to retrive data :"))
   

    
    try:
        connection = psycopg2.connect(database='scanner', user='scan', password='password', host='127.0.0.1', port= '5432')
        cursor = connection.cursor()
        if ID==1:
            output = subprocess.getoutput('''sudo -u postgres psql scanner -c "select id,file_name,time_stamp  from Trivy"''')
            print(output)
            fetch_id=int(input("Enter your choice to fetch report:"))
            post_query = """SELECT * from Trivy where Id = %s"""
            cursor.execute(post_query, (fetch_id,))
            record = cursor.fetchall()
            for row in record:
                file = row[3]
                d_path=path+"/db_reports/Trivy/"+row[1]+".txt"
                #print(d_path)
                write_file(file,d_path)
            os.chdir(path)
            os.system("cat {}".format(d_path))
            print("Storing employee image and bio-data on disk  {} \n".format(d_path))
                
        if ID==2:
             
             
            output = subprocess.getoutput('''sudo -u postgres psql scanner -c "select id,file_name,time_stamp  from Clair"''')
            print(output)
            fetch_id=int(input("Enter your choice to fetch report :"))
           
            post_query = """SELECT * from Clair where Id = %s"""
            cursor.execute(post_query, (fetch_id,))
            record = cursor.fetchall()
            for row in record:
                 file = row[3]
                 d_path=path+"/db_reports/clair/"+row[1]+".txt"
                 #print(d_path)
                 write_file(file,d_path)
            os.system("cat {}".format(d_path))
            print("Storing employee image and bio-data on disk  {} \n".format(d_path))
            os.chdir(path)  
                
        if ID==3:
            output = subprocess.getoutput('''sudo -u postgres psql scanner -c "select id,file_name,time_stamp  from Grype"''')
            print(output)
            fetch_id=int(input("Enter your choice to fetch report:"))
            post_query = """SELECT * from Grype where Id = %s"""
            cursor.execute(post_query, (fetch_id,))
            record = cursor.fetchall()
            for row in record:
                file = row[3]
                d_path=path+"/db_reports/grype/"+row[1]+".txt"
                #print(d_path)                
                write_file(file,d_path)
            os.system("cat {}".format(d_path))
            print("Storing employee image and bio-data on disk  {} \n".format(d_path))
            os.chdir(path)
                
        if ID==4:
            output = subprocess.getoutput('''sudo -u postgres psql scanner -c "select id,file_name,time_stamp  from Combine"''')
            print(output)
            fetch_id=int(input("Enter your choice to fetch report:"))
            post_query = """SELECT * from Combine where Id = %s"""
            cursor.execute(post_query, (fetch_id,))
            record = cursor.fetchall()
            for row in record:
                file = row[3]
                d_path=path+"/db_reports/combine/"+row[1]+".txt"
                #print(d_path)
                write_file(file,d_path)
            os.system("cat {}".format(d_path))
            print("Storing employee image and bio-data on disk  {} \n".format(d_path))
            os.chdir(path)    
             
        if ID==5:
            exit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Failed inserting  data into Postgres table {}".format(error))
    
    
    


    

def creation():
   
    os.system("sudo -u postgres createdb scanner")
    os.system("sudo -u postgres createuser scan")
    
    order='''sudo -u postgres psql -c "alter user scan with password 'password'"'''
    os.system(order)  
    order1='''sudo -u postgres psql -c "grant all privileges on database scanner to scan"'''
    os.system(order1)
    connection = psycopg2.connect(database='scanner', user='scan', password='password', host='127.0.0.1', port= '5432')
    print("connetion successful")
    #connection = psycopg2.connect(database='scanner', user='scan', password='password', host='127.0.0.1', port= '5432')
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Trivy")
    cursor.execute("DROP TABLE IF EXISTS Clair")
    cursor.execute("DROP TABLE IF EXISTS Grype")
    cursor.execute("DROP TABLE IF EXISTS Combine")
    sql ='''CREATE TABLE Trivy(ID  SERIAL PRIMARY KEY,file_name text, Time_stamp text,file bytea)'''
    cursor.execute(sql)
    sql1 ='''CREATE TABLE Clair(ID  SERIAL PRIMARY KEY,file_name text, Time_stamp text,file bytea)'''
    cursor.execute(sql1)
    sql2 ='''CREATE TABLE Grype(ID  SERIAL PRIMARY KEY,file_name text, Time_stamp text,file bytea)'''
    cursor.execute(sql2)
    sql3='''CREATE TABLE Combine(ID  SERIAL PRIMARY KEY,file_name text, Time_stamp text,file bytea)'''
    cursor.execute(sql3)
    print("Table created successfully........")   
    
def connection():
    os.system("sudo systemctl start postgresql")
    Check=str(input(red("Are you creating database for first time (y|n):","bold")))
    if Check=='y' or Check=='Y':
        creation()
    else:
        C=str(input(blue( 'DO you delete previous one and create new one again (y|n):','bold')))
        #output = subprocess.getoutput('''sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='scanner'"''')
        #if output=="1":
        if C=='y' or C=='Y':
              os.system("sudo -u postgres dropdb scanner")
              os.system("sudo -u postgres dropuser scan")
              creation()
        else:
            pass
