from states import state

class JobExecutionState(state.State):

	def __init__(self, client):
		super().__init__(client)


	def receive_ok(self):
		self.client.s.send("REDY".encode())


	def receive_none(self):
		self.client.s.send("QUIT".encode())
		self.client.setState(self.client.getQuitState())


	def receive_job_request(self, params):
		self.client.s.send(' '.join(["RESC", "Avail",  params[3], params[4], params[5]]).encode())
		resource_information = []
		data = self.client.s.recv(1024).decode()
		while data != ".":
			if(data == "DATA"):
				self.client.s.send("OK".encode())
			else:
				resource_information.append(data.split())
				self.client.s.send("OK".encode())
			data = self.client.s.recv(1024).decode()

		executing_server = self.client.getServer(resource_information)
		dataSend = " ".join(["SCHD", params[1], executing_server, "0"])
		self.client.s.send(dataSend.encode())

