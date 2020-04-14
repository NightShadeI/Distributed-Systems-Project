from states import state

class AuthenticationState(state.State):

	def __init__(self, client):
		super().__init__(client)


	def receive_ok(self):
		self.client.readSystemData()
		self.client.s.send("REDY".encode())
		self.client.setState(self.client.getJobExecutionState())