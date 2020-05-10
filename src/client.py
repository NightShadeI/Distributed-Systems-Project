#!/usr/bin/env python

import socket
import sys
import argparse
from states import *
from strategies import *


class Client:

    def __init__(self):
        self.startState = start.StartState(self)
        self.authState = authentication.AuthenticationState(self)
        self.jobExecutionState = jobexecution.JobExecutionState(self)
        self.quitState = quitstate.QuitState(self)
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


    def checkParams(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', required=True, help="specify algorithm")
        args = parser.parse_args()
        if args.a:
            if args.a == "ff":
                self.serverStrategy = firstfit.FirstFit()
            elif args.a == "bf":
                self.serverStrategy = bestfit.BestFit()
            elif args.a == "wf":
                self.serverStrategy = worstfit.WorstFit()
            else:
                print("Invalid algorithm")
                sys.exit(1)


    def run(self):
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
    client.checkParams()
    client.run()


