import socket
import sys

s = socket.socket()
s.connect(('127.0.0.1', 50000))

s.send('HELO'.encode())
data = s.recv(1024).decode()
if(data == 'OK'):
  s.send('AUTH comp335'.encode())
  data = s.recv(1024).decode()
  if(data == 'OK'):
    s.send('REDY'.encode())
s.close()

