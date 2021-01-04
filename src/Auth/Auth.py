import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'minapi'

class Auth:
	def __init__(self, token):
		self.token = token

	@staticmethod
	def generate_token(email):
		exp = datetime.now() + timedelta(seconds=120)
		return jwt.encode({"email": email, "exp": exp}, SECRET_KEY, algorithm='HS256')

	def auth(self):
		try:
			data = jwt.decode(self.token, SECRET_KEY, algorithms=["HS256"])
			return data
		except jwt.ExpiredSignatureError:
			return False