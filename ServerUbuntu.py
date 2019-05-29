#!/usr/local/bin/python3
import subprocess
import socket
hostname = socket.gethostname() #to get the computers hostname
IPAddr = socket.gethostbyname(hostname)  #to get computers ip address
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)
print ("starting server ......")
subprocess.run(["/usr/bin/iperf3","-s","-i","1","-1"])
