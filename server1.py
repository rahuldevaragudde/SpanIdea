#!/usr/local/bin/python3
# import subprocess
# import os
# import socket
# var = 'iperf3.json'
# os.path.abspath(var)
# hostname = socket.gethostname() #to get the computers hostname    
# IPAddr = socket.gethostbyname(hostname)  #to get computers ip address  
# print("Your Computer Name is:" + hostname)    
# print("Your Computer IP Address is:" + IPAddr)
# print ("starting server ......")
# subprocess.run([var,"-s","-i","1","-1"])

##########################
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    essid=input("enetr the essid:").strip()
    password=input("enter the password:").strip()

    print('connecting to network ' + essid + '...')
    wlan.connect(essid, password)
    # connect() appears to be async - waiting for it to complete
    while not wlan.isconnected():
        print('waiting for connection...')
        utime.sleep(4)
        print('checking connection...')
    print('Wifi connect successful, network config: %s' % repr(wlan.ifconfig()))
else:
        # Note that connection info is stored in non-volatile memory. If
        # you are connected to the wrong network, do an explicity disconnect()
        # and then reconnect.
    print('Wifi already connected, network config: %s' % repr(wlan.ifconfig()))

