from ..Database import Database
from ..Auth import Auth
from .users import users
import uuid

class contacts:
	def __init__(self, contact_name = None, contact_phone_number = None, contact_email = None, contact_address = None, contact_id = None, user_id = None):
		self.contact_id = contact_id
		self.contact_name = contact_name
		self.contact_phone_number = contact_phone_number
		self.contact_email = contact_email
		self.contact_address = contact_address
		self.user_id = user_id

	def __str__(self):
		return ''.join(f"{attr}: {value}, " for attr, value in self.__dict__.items())[:-2]


	@staticmethod
	@Auth.authenticate
	def get_all(**kwargs):
		email = kwargs.get('email')
		user = users.get_by_id(email)
		sql = f"SELECT * FROM contacts WHERE user_id = '{user.user_id}'"
		db = Database()
		rs = db.execute(sql)
		return rs.rows

	@Auth.authenticate
	def get_by_id(self, **kwargs):
		email = kwargs.get('email')
		user = users.get_by_id(email)
		sql = f"SELECT * FROM contacts WHERE user_id = '{user.user_id}' AND contact_id = '{self.contact_id}'"
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
		db = Database()
		rs = db.execute(sql)

	@Auth.authenticate
	def update(self, **kwargs):
		email = kwargs.get('email')
		user = users.get_by_id(email)
		sql = f"UPDATE contacts SET \
			contact_name = '{self.contact_name}', \
			contact_phone_number = '{self.contact_phone_number}', \
			contact_email = '{self.contact_email}', \
			contact_address = '{self.contact_address}' \
			WHERE user_id = '{user.user_id}' AND \
			contact_id = '{self.contact_id}'\
		".replace('\t', '')
		db = Database()
		rs = db.execute(sql)

	@Auth.authenticate
	def delete(self, **kwargs):
		email = kwargs.get('email')
		user = users.get_by_id(email)
		sql = f"DELETE FROM contacts \
			WHERE user_id = '{user.user_id}' AND \
			contact_id = '{self.contact_id}'\
		".replace('\t', '')
		db = Database()
		rs = db.execute(sql)
