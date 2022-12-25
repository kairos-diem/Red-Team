#!/bin/bash/python3

import sys
import socket
from datetime import datetime
import re

#regex check for valid Ip address
regexIP = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''


#define your target
if len(sys.argv) == 2: 
    if re.search(regexIP,sys.argv[1]):
        target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
    else:
        print("Invalid IP address, enter propper IPv4 address.")
        sys.exit()
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

#Add a pretty banner
print("-" * 50)
print("Scanning Target:" + target)
print("Time Started:" + str(datetime.now()))
print("-" * 50)

try: 
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()

