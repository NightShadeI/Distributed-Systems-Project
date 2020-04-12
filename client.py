#!/usr/bin/env python

import socket
import sys
import xml.etree.ElementTree as ET

def biggestserver(node):
  if(node[0].tag == 'servers'):
    biggest = int(node[0][0].attrib['coreCount'])
    indexFinal = int(0)
    tempIndex = int(0)
    for child in node[0]:
        if(int(child.attrib['coreCount']) > biggest):
            indexFinal = tempIndex
            biggest = int(child.attrib['coreCount'])
        tempIndex+=1
  return node[0][indexFinal].attrib['type']

if __name__ == "__main__":
  s = socket.socket()
  s.connect(('127.0.0.1', 50000))

  s.send('HELO'.encode())
  data = s.recv(1024).decode()
  if(data == 'OK'):
    s.send('AUTH root'.encode())
    data = s.recv(1024).decode()

  biggestServerName = biggestserver(ET.parse('system.xml').getroot())
  start = True

  while (data == 'OK'):
    if start:
      s.send('REDY'.encode())
      start = False
    data = s.recv(1024).decode()
    if data.split()[0] == 'JOBN':
      s.send(('SCHD ' + data.split()[2] + ' ' + biggestServerName + ' 0').encode())
      data = s.recv(1024).decode()
      s.send('REDY'.encode())
    elif data.split()[0] == 'NONE':
      s.send('QUIT'.encode())
      data = s.recv(1024).decode()
      #test2
  s.close()
