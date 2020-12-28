from Database import Database

class users:
	def __init__(self, uuid, email, password):
		self.user_id = uuid
		self.email = email
		self.password = password

	@staticmethod
	def get_all():
		pass