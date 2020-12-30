from .DbConnection import DbConnection
import re

class Database:
	def __init__(self, conn=None):
		self.conn = conn

	def make_connection(func):
		def decorator(self, sql):
			self.conn = DbConnection()
			self.conn = self.conn.connect()
			self.conn.commit()
			rs = func(self, sql)
			self.conn.commit()
			self.conn.close()
			return rs
		return decorator

	@make_connection
	def execute(self, sql):
		if self.conn is not None:
			with self.conn.cursor() as cursor:
				cursor.execute(sql)

				select_pattern = re.compile(r'^select', re.IGNORECASE)
				if(re.search(select_pattern, sql)):
					return Database.Results(cursor)

				insert_pattern = re.compile(r'^insert', re.IGNORECASE)
				if(re.search(insert_pattern, sql)):
					return "Success"

	class Results:
		def __init__(self, cursor):
			self.cursor = cursor
			self.header = self.get_header()
			self.rows = self.get_rows()

		def get_header(self):
			return [column[0] for column in self.cursor.description]

		def get_rows(self):
			return [dict((self.cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in self.cursor.fetchall()]
