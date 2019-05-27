#!/usr/local/bin/python3
import subprocess
import sys
server=sys.argv[1]
#print("connecting to ", server)
subprocess.run(["/usr/local/bin/iperf3","-c", server, "-i", "1", "-t", "10","-b","0","-P","5","-O","2"]) 
