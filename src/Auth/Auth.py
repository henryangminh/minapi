import jwt
from datetime import datetime, timedelta, timezone
from ..utils.constant import SECRET_KEY


class Auth:
	def __init__(self, token = None):
		self.token = token

	@staticmethod
	def generate_token(email):
		exp = int((datetime.now(tz=timezone.utc) + timedelta(seconds=120)).timestamp())
		return jwt.encode({"email": email, "exp": exp}, SECRET_KEY, algorithm='HS256')

	def auth(self):
		try:
			data = jwt.decode(self.token, SECRET_KEY, algorithms=["HS256"])
			return True, data
		except jwt.ExpiredSignatureError:
			return False, 'Token is expired'
		except jwt.InvalidIssuerError:
			return False, 'Invalid token'
		except jwt.DecodeError:
			return False, 'Decode Error'

	# @staticmethod
	# def authenticate(token):
	# 	def decorator(func):
	# 		def wrap(p):
	# 			auth = Auth(token)
	# 			if(auth.auth()):
	# 				func(p)
	# 		return wrap
	# 	return decorator

	@staticmethod
	def authenticate(func):
		def decorator(auth):
			rs, response = auth.auth()
			if(rs):
				func(response.get("email"))
			else:
				print(response)

		return decorator
