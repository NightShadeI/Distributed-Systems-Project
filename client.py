#!/usr/bin/env python2.7

import socket
import sys
import xml.etree.ElementTree as ET

def biggestserver(node):
    if(node[0].tag == 'servers'):
        biggest = int(node[0][0].attrib['coreCount'])
        for child in enumerate(node[0]):
            currchild = int(child[1].attrib['coreCount'])
            if(currchild > biggest):
                biggest = child        
    return node[0][child[0]].attrib['type']        


if __name__ == "__main__":
    s = socket.socket()
    s.connect(('127.0.0.1', 50000))
    s.send("HELO".encode())
    data = s.recv(1024).decode()
    
    if(data == "OK"):
        s.send("AUTH root".encode())
        data = s.recv(1024).decode()
        s.send("REDY".encode())

    biggestServerName = biggestserver(ET.parse('system.xml').getroot())

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
