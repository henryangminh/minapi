from http.server import BaseHTTPRequestHandler
import json
import re
from src.Model import users
from src.Database import Database
from src.utils.json_utils import to_dict


#Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
	#sets basic headers for the server
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/json')
		#reads the length of the Headers
		length = int(self.headers['Content-Length'])
		#reads the contents of the request
		content = self.rfile.read(length)
		temp = content.decode()
		temp = to_dict(temp)
		self.end_headers()
		return temp

	######
	#LIST#
	######
	#GET Method Defination
	def do_GET(self):
		#defining all the headers
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		#prints all the keys and values of the json file
		path = self.path

		if(path=='/'):
			self.wfile.write('Welcome to minapi'.encode())

		user_pattern = re.compile(r'/user$')
		if(re.search(user_pattern, path)):
			rs = users.get_all()
			rs_json = json.dumps(rs)
			self.wfile.write(rs_json.encode())

		user_pattern_id = re.compile(r'/user/\w+')
		if(re.search(user_pattern_id, path)):
			rs = users.get_by_id(path.split('/')[-1])
			rs_json = json.dumps(rs)
			self.wfile.write(rs_json.encode())

	######
	#VIEW#
	######
	#VIEW method defination
	# def do_VIEW(self):
	# 	#dict var. for pretty print
	# 	display = {}
	# 	temp = self._set_headers()
	# 	#check if the key is present in the dictionary
	# 	if temp in data:
	# 		display[temp] = data[temp]
	# 		#print the keys required from the json file
	# 		self.wfile.write(json.dumps(display).encode())
	# 	else:
	# 		error = "NOT FOUND!"
	# 		self.wfile.write(bytes(error,'utf-8'))
	# 		self.send_response(404)

	########
	#CREATE#
	########
	#POST method defination
	def do_POST(self):
		path = self.path
		if(path=='/'):
			self.wfile.write('Welcome to minapi'.encode())

		temp = self._set_headers()

		user_pattern = re.compile(r'/register$')
		if(re.search(user_pattern, path)):
			users.insert(temp)

		login_pattern = re.compile(r'/login$')
		if(re.search(login_pattern, path)):
			user = users(temp)
			user.check_login()


	########
	#UPDATE#
	########
	#PUT method Defination
	def do_PUT(self):
		path = self.path
		if(path=='/'):
			self.wfile.write('Welcome to minapi'.encode())

		temp = self._set_headers()

		change_email_pattern = re.compile(r'/change_email$')
		if(re.search(change_email_pattern, path)):
			users.change_email(temp)

		change_pass_pattern = re.compile(r'/change_pass$')
		if(re.search(change_pass_pattern, path)):
			users.change_pass(temp)


	########
	#DELETE#
	########
	#DELETE method defination
	def do_DELETE(self):
		path = self.path
		if(path=='/'):
			self.wfile.write('Welcome to minapi'.encode())

		temp = self._set_headers()

		delete_user_pattern = re.compile(r'/delete_user$')
		if(re.search(delete_user_pattern, path)):
			users.delete(temp.get('user_id'))
