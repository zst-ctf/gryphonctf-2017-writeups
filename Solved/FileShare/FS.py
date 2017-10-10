
#!/usr/bin/env python3
import base64
import ast
from datetime import datetime
import time
import os
import socket
import threading
import random
import traceback
def check(stri):
    k=0
    for i in stri:
        k=k+ord(i)
    return k
def filename():
   return ''.join(random.choice("QWERTYUIOPASDFGHJKLZXCVBNM") for i in range(3))
def create(line,nam,c):
    k="/home/fileshare/"
    name="files/"+filename()
    f=open(k+name,"w")
    print(line,file=f)
    n=[name,nam]
    k=str(n)
    return base64.b64encode(k.encode()).decode()
def gets(filename,c):
    kul="/home/fileshare/"
    try:
        kkkk=base64.b64decode(filename).decode()
        l=ast.literal_eval(kkkk)
        if len(l)==2 and len(l[1])>=3:
            c.sendall("~~~~~~~~~~~~~~~~~~~~~~~~\n\nFILE FROM: {}\nFILE CONTENTS: \n\n".format(l[1]).encode())
            f=open(kul+l[0],"r")
            jj=f.readlines()
            for i in jj:
               z=i
               c.sendall(z.encode())
            c.sendall("\n\n~~~~~~~~~~~~~~~~~~~~~~~~\n\n".encode())
        else:
            c.sendall("INVALID KEY!\n".encode())
    except Exception as e:
        error=traceback.format_exc()
        c.sendall(error.encode())
        z="Wrong key, no such file\n"
        c.sendall(z.encode())
    

def start(c,a,user):
    kkk="QQTLBFVLZFCJHABTKQWYYTBLTLNENP"
    try:
        c.sendall('''
          `ohmmmmmmmmmmmmmmmmmh:
Received: -NMMhyyyyyyyyyyyyyyNMMMd:                
         sMMo               mMMNMMd:              
         sMMo               mMM-+mMMd:            
         sMMo               mMM/.-sMMMd:          
         sMMo               mMMMMMMMMMMMo         
         sMMo               :////////yMMs         
         sMMo                        oMMs         
         sMMo                        oMMs         
         sMMo                        oMMs         
         sMMo                        oMMs         
         sMMo                        oMMs         
         sMMo                        oMMs
         oMMs                        oMMs
         oMMs                        oMMs
         sMMo                        oMMs         
         sMMo                        oMMs         
         sMMo                        oMMs         
         sMMo                        oMMs         
         -NMMhyyyyyyyyyyyyyyyyyyyyyyhMMN-         
          `ohmmmmmmmmmmmmmmmmmmmmmmmmho`          

YOU ARE ZE NO.{} USER
WELCOME TO THE GREATEST FILE SHARING SERVICE IN ALL OF ZE WORLD!
           a)  CREATE FILE
           b)  VIEW FILE
YOUR INPUT => '''.format(user).encode())
        c.settimeout(2*60)
        r=c.recv(100).decode().strip()
        if r=="a":
            c.sendall("YOU HAVE CHOSEN TO MAKE FILE!\nPLEASE INPUT NAME!(3-5 CHARAS ONLY) => ".encode())
            c.settimeout(60*2)
            nam=c.recv(135).decode().strip()
Received: c.sendall("PLEASE INPUT MESSAGE  => ".encode())
            lll=c.recv(125).decode().strip()
            print(len(nam))
            print(len(lll))
            if len(lll)>130 or (len(nam)<3 or len(nam)>5):
                c.sendall("sorry invalid input :(\n".encode())
                c.sendall("GOODBYE!\n".encode())
                c.close()
            else:
                key=create(lll,nam,c)
                z="FILES CREATED! HERE IS YOUR KEY "+key
                c.sendall(z.encode())
                c.sendall("\nGOODBYE!\n".encode())
                c.close()
        elif r=="b":
            c.sendall("YOU HAVE CHOSEN TO VIEW FILE\nPLEASE INPUT KEY! => ".encode())
            c.settimeout(60*2)
            lll=c.recv(100).decode().strip()
            if(len(lll)>33):
                c.sendall("KEY TOO LONG, INVALID\nGOODBYE\n".encode())
                c.close()
            else:
                gets(lll,c)
                c.sendall("GOODBYE!\n".encode())
                c.close()
        elif r==kkk:
            f=open("/home/fileshare/flag/thisisalongnameforadirectoryforareasonflag.txt","r")
            k=f.readline()
            z="HELLO ADMINISTRATOR!\n~~~WELCOME TO THE ADMIN PORTAL~~~\n           a)  LIST ALL FILES\n           b)  PRINT FLAG\nYOUR INPUT => "
            c.sendall(z.encode())
            c.settimeout(60*2)
            h=c.recv(3).decode().strip()
            if h=="a":
                k=os.listdir("/home/fileshare/files/")
                for i in k:
                    i="- "+i+"\n"
                    c.sendall(i.encode())
                c.sendall("GOODBYE\n".encode())
            elif h=="b":
                c.sendall("PASSWORD PLS ! =>".encode())
                c.settimeout(60*2)
                z=c.recv(10).decode().strip()
                if int(z)==check("REALADMIN"):
                    c.sendall("HERES THE FLAG!\n".encode())
                    c.sendall(k.encode())
                else:
                    c.sendall("YOU ARE NOT REAL ADMIN! BYE\n".encode())
            else:
                c.sendall("INVALID!\nGOODBYE!\n".encode());
            c.close()
        else:
            c.sendall("invalid input!\n".encode())
            c.close()
    except Exception as e:
        error=traceback.format_exc()
        c.sendall(error.encode())
        c.close()

        
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('0.0.0.0',49760))
print(socket)
socket.listen(5)
user=0
while True:
    c,a=socket.accept()
    user=user+1
    t=threading.Thread(target=start,args=(c,a,user))
    t.start()
socket.close()


