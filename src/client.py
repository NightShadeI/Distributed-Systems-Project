#!/usr/bin/env python

import socket
import xml.etree.ElementTree as ET
from states import *

def biggestserver(servers):
    biggest_server = servers[0]
    for server in servers:
        if int(server.attrib['coreCount']) > int(biggest_server.attrib['coreCount']):
            biggest_server = server        
    return biggest_server.attrib['type']

class Client:

    def __init__(self):
        self.startState = start.StartState(self)
        self.authState = authentication.AuthenticationState(self)
        self.jobExecutionState = jobexecution.JobExecutionState(self)
        self.quitState = quitstate.QuitState(self)
        self.serverOptimiser = biggestserver
        self.setState(self.getStartState())


    def setState(self, state):
        self.state = state


    def getStartState(self):
        return self.startState


    def getAuthenticationState(self):
        return self.authState


    def getJobExecutionState(self):
        return self.jobExecutionState


    def getQuitState(self):
        return self.quitState


    def readSystemData(self):
        self.tree = ET.parse('../simulator/system.xml')


    def getServer(self):
        # Not fully implemented yet
        server = self.serverOptimiser(self.tree.getroot().find("servers"))
        return server


    def buildSocket(self):
        self.s = socket.socket()
        self.s.connect(('127.0.0.1', 50000))


    def closeSocket(self):
        self.s.close()


    def run(self):
        self.buildSocket()
        self.s.send("HELO".encode())
        while True:
            data = s.recv(1024).decode()
            if data.startswith("OK"):
                self.state.receive_ok()
            elif data.startswith("NONE"):
                self.state.receive_none()
            elif data.startswith("JOBN"):
                self.state.receive_job_request(data.split()[1:])
            elif data.receive_quit("QUIT"):
                self.state.receive_quit()


if __name__ == "__main__":
    
    client = Client()
    client.run()


