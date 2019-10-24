#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
subprocess.call('clear' , shell=True)
remoteServer = raw_input("Enter a remote host name Or IP \n")

remoteServerIp = socket.gethostbyname(remoteServer)

print "-"*60
print "please wait Scanning remote host",remoteServerIp
print "-"*60

t1 = datetime.now()
#1025
try:
    for port in range(1,65535):
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        reult = sock.connect_ex((remoteServerIp , port))
        if reult == 0:
            print"Port {}: Open".format(port)
            sock.close()
            
except KeyboardInterrupt:
    print"You pressed CTRL+C"
    sys.exit()

except socket.gaierror:
    print"Host name couldnit be resolved"
    sys.exit()

except socket.error:
    print"couldnt connect to server"
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print"scanning completed in:",total
