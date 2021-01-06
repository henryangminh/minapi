import jwt
from datetime import datetime, timedelta, timezone
from ..Model.users import users
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
			return data
		except jwt.ExpiredSignatureError:
			return False
		except jwt.InvalidIssuerError:
			return False

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
			rs = auth.auth()
			if(rs):
				user = users(users.get_by_id(rs.get("email"))[0])
				func(user)
			else:
				print('timeout')

		return decorator
