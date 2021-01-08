from ..Database import Database
from ..Auth import Auth
from .users import users
import uuid

class contacts:
	def __init__(self, contact_name, contact_phone_number, contact_email, contact_address, contact_id = None, user_id = None):
		self.contact_id = contact_id
		self.contact_name = contact_name
		self.contact_phone_number = contact_phone_number
		self.contact_email = contact_email
		self.contact_address = contact_address
		self.user_id = user_id

	def __str__(self):
		return ''.join(f"{attr}: {value}, " for attr, value in self.__dict__.items())[:-2]

	# @staticmethod
	# def get_all(email):
	# 	sql = f"SELECT * FROM contacts WHERE email = '{email}'"
	# 	db = Database()
	# 	rs = db.execute(sql)
	# 	return rs.rows

	@staticmethod
	@Auth.authenticate
	def get_all(**kwargs):
		# user = users(users.get_by_id(email)[0])
		# print(user.user_id)
		email = kwargs.get('email')
		sql = f"SELECT * FROM contacts WHERE email = '{email}'"
		db = Database()
		rs = db.execute(sql)
		return rs.rows

	@Auth.authenticate
	def insert(self, **kwargs):
		email = kwargs.get('email')
		user = users.get_by_id(email)
		self.contact_id = uuid.uuid1()
		sql = f"INSERT INTO contacts (contact_id, contact_name, contact_phone_number, contact_email, contact_address, user_id) VALUES \
		(\
			'{self.contact_id}', \
			'{self.contact_name}', \
			'{self.contact_phone_number}', \
			'{self.contact_email}', \
			'{self.contact_address}', \
			'{user.user_id}'\
		)".replace('\t', '')
		# print(sql)
		db = Database()
		rs = db.execute(sql)
