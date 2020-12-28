# from DbConnection import DbConnection

# db = DbConnection()

class Database:
	def __init__(self, conn):
		self.conn = conn

	def make_connection(func):
		def decorator(self, sql):
			self.conn.commit()
			rs = func(self, sql)
			self.conn.close()
			return rs
		return decorator

	@make_connection
	def execute(self, sql):
		if self.conn is not None:
			with self.conn.cursor() as cursor:
				cursor.execute(sql)
				a = cursor.fetchall()
				print(a)
				return Database.Results(cursor)

	class Results:
		def __init__(self, cursor):
			self.cursor = cursor
			self.header = self.get_header()
			# self.rows = self.get_rows()

		def get_header(self):
			return [column[0] for column in self.cursor.description]

		# def get_rows(self):
		# 	rs = []
		# 	for rows in self.cursor.fetchall():
		# 		row = [key for key in rows]
		# 		rs.append(row)

		# 	return rs