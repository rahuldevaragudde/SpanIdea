#!/usr/local/bin/python3
import subprocess
import os
import socket
var = 'iperf3.json'
os.path.abspath(var)
hostname = socket.gethostname() #to get the computers hostname    
IPAddr = socket.gethostbyname(hostname)  #to get computers ip address  
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)
print ("starting server ......")
subprocess.run([var,"-s","-i","1","-1"])

