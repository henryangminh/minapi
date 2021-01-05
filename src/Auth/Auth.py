import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = 'minapi'

class Auth:
	def __init__(self, token = None):
		self.token = token

	@staticmethod
	def generate_token(email):
		exp = int(datetime.now(tz=timezone.utc).timestamp() * 1000) + timedelta(seconds=120)
		return jwt.encode({"email": email, "exp": exp}, SECRET_KEY, algorithm='HS256')

	def auth(self):
		try:
			data = jwt.decode(self.token, SECRET_KEY, algorithms=["HS256"], options={"verify_exp": True})
			return data
		except jwt.ExpiredSignatureError:
			return False

	@staticmethod
	def authenticate(token):
		def decorator(func):
			def wrap(p):
				print(token)
				func(p)
			return wrap
			# auth = Auth(token)
			# if(auth.auth()):
			# 	func(*args)

		return decorator
