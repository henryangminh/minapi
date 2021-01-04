from ..Database import Database
import json
import uuid
import hashlib
import jwt
from datetime import datetime, timedelta
from ..Auth import Auth

SECRET_KEY = 'minapi'

class users:
	def __init__(self, dictionary):
		vars(self).update(dictionary)

	@staticmethod
	def to_objects(rows):
		rs = []
		for row in rows:
			user = users.to_object(row)
			rs.append(user)
		return rs

	@staticmethod
	def to_object(row):
		json_object=str(row).replace('\'','"')
		a = json.loads(json_object, object_hook=users)
		return a

	@staticmethod
	def get_all():
		sql = "SELECT * FROM users"
		db = Database()
		rs = db.execute(sql)
		return rs.rows

	def __str__(self):
		return ''.join(f"{attr}: {value}, " for attr, value in self.__dict__.items())[:-2]

	@staticmethod
	def get_by_id(id):
		sql = f"SELECT * FROM users WHERE user_id = '{id}'"
		db = Database()
		rs = db.execute(sql)
		return rs.rows

	@staticmethod
	def get_by_email(email):
		sql = f"SELECT * FROM users WHERE email = '{email}'"
		db = Database()
		rs = db.execute(sql)
		return rs.rows

	@staticmethod
	def insert(user_dict):
		user = users(user_dict)
		user.email = user.email.lower()
		user.user_id = uuid.uuid1()
		user.password = hashlib.md5(user.password.encode()).hexdigest()
		sql = f"INSERT INTO users (user_id, email, password) VALUES ('{user.user_id}', '{user.email}', '{user.password}');"
		db = Database()
		db.execute(sql)

	@staticmethod
	def change_email(user_dict):
		user = users(user_dict)
		user.email = user.email.lower()
		sql=f"UPDATE users SET email = '{user.email}' WHERE user_id = '{user.user_id}'"
		db = Database()
		db.execute(sql)

	@staticmethod
	def change_pass(user_dict):
		user = users(user_dict)
		user.password = hashlib.md5(user.password.encode())
		sql=f"UPDATE users SET password = '{user.password}' WHERE user_id = '{user.user_id}'"
		db = Database()
		db.execute(sql)

	@staticmethod
	def delete(id):
		sql = f"DELETE FROM users WHERE user_id = '{id}' OR email = '{id}'"
		db = Database()
		db.execute(sql)

	def check_login(self):
		user_temp = users.get_by_email(self.email)
		user_temp = users.to_object(user_temp[0])
		return True if user_temp.password == hashlib.md5(self.password.encode()).hexdigest() else False

	def generate_token(self):
		if(self.check_login()):
			return Auth.generate_token(self.email)
			# print(token)
			# untoken = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
			# print(untoken)
