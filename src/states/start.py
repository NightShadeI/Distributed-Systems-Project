from states import state

class StartState(state.State):

	def __init__(self, client):
		super().__init__(client)
		self.creds = "root"


	def receive_ok(self):
		self.client.s.send("AUTH {}".format(self.creds).encode())
		self.client.setState(self.client.getAuthenticationState())