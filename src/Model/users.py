from ..Database import Database
import json

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
		print(str(a))
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
	def insert(user):
		sql = f"INSERT INTO users (user_id, email, password) VALUES {user.user_id}, {user.email}, {user.password}"
		db = Database()
		rs = db.execute(sql)
		
