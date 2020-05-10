#!/usr/bin/env python

import socket
import sys
from states import *
from strategies import *


class Client:

    def __init__(self):
        self.startState = start.StartState(self)
        self.authState = authentication.AuthenticationState(self)
        self.jobExecutionState = jobexecution.JobExecutionState(self)
        self.quitState = quitstate.QuitState(self)
        self.serverStrategy = firstfit.FirstFit()
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
        self.serverStrategy.readSystemData()


    def getServer(self, params):
        server = self.serverStrategy.calculate(params)
        return server


    def buildSocket(self):
        self.s = socket.socket()
        self.s.connect(('127.0.0.1', 50000))


    def closeSocket(self):
        self.s.close()


    def run(self):
        if len(sys.argv) < 3:
            sys.exit("Not enough arguments (have you specified a strategy?)")
        self.buildSocket()
        self.s.send("HELO".encode())
        while True:
            data = self.s.recv(1024).decode()
            if data.startswith("OK"):
                self.state.receive_ok()
            elif data.startswith("NONE"):
                self.state.receive_none()
            elif data.startswith("JOBN"):
                self.state.receive_job_request(data.split()[1:])
            elif data.startswith("QUIT"):
                self.state.receive_quit()
            else:
                print("Unknown command", flush=True)
                break


if __name__ == "__main__":
    
    client = Client()
    client.run()


