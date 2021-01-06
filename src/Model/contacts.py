from ..Database import Database
from ..Auth import Auth
from .users import users

class contacts:
	def __init__(self, contact_id, name, phone_no, email, address, uuid):
		self.contact_id = contact_id
		self.name = name
		self.phone_no = phone_no
		self.email = email
		self.address = address
		self.user_id = uuid

	@staticmethod
	def get_all(email):
		sql = f"SELECT * FROM contacts WHERE email = '{email}'"
		db = Database()
		rs = db.execute(sql)
		return rs.rows

	@staticmethod
	@Auth.authenticate
	def get_alls(email):
		user = users(users.get_by_id(email)[0])
		print(user.user_id)
