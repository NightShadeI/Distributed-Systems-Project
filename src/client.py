#!/usr/bin/env python

import socket
import sys
import xml.etree.ElementTree as ET

def biggestserver(servers):
    biggest_server = servers[0]
    for server in servers:
        if int(server.attrib['coreCount']) > int(biggest_server.attrib['coreCount']):
            biggest_server = server        
    return biggest_server.attrib['type']        


if __name__ == "__main__":
    
    s = socket.socket()
    s.connect(('127.0.0.1', 50000))
    s.send("HELO".encode())
    data = s.recv(1024).decode()
    
    if(data == "OK"):
        s.send("AUTH root".encode())
        data = s.recv(1024).decode()
        s.send("REDY".encode())

    biggestServerName = biggestserver(ET.parse('system.xml').getroot().find("servers"))

    while (data == "OK"):
        data = s.recv(1024).decode() 
        if data.startswith("JOBN"):
            dataSend = " ".join(["SCHD",data.split()[2],biggestServerName,"0"])
            s.send(dataSend.encode())
            data = s.recv(1024).decode()
            s.send("REDY".encode())
        elif data.startswith("NONE"):
            s.send("QUIT".encode())
            data = s.recv(1024).decode()
    
    s.close()
