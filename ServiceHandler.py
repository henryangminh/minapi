from http.server import BaseHTTPRequestHandler
import json
import re
from src.Auth import Auth
from src.Database import Database
from src.Model import users, contacts
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
		#prints all the keys and values of the json file
		path = self.path

		if(path=='/'):
			self.wfile.write('Welcome to minapi'.encode())

		user_pattern = re.compile(r'/user$')
		if(re.search(user_pattern, path)):
			#defining all the headers
			self.send_response(200)
			self.send_header('Content-type','text/json')
			self.end_headers()

			rs = users.get_all()
			rs_json = json.dumps(rs)
			self.wfile.write(rs_json.encode())

		user_pattern_id = re.compile(r'/user/\w+')
		if(re.search(user_pattern_id, path)):
			#defining all the headers
			self.send_response(200)
			self.send_header('Content-type','text/json')
			self.end_headers()

			rs = users.get_by_id(path.split('/')[-1])
			rs_json = json.dumps(rs)
			self.wfile.write(rs_json.encode())

		contact_pattern = re.compile(r'/contacts$')
		if(re.search(contact_pattern, path)):
			temp = self._set_headers()
			contacts.get_all(token = temp.get('token'))

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
			user = users(temp)
			user.insert()

		login_pattern = re.compile(r'/login$')
		if(re.search(login_pattern, path)):
			user = users(temp)
			self.wfile.write(user.generate_token().encode())

		oauth_pattern = re.compile(r'/oauth$')
		if(re.search(oauth_pattern, path)):
			auth = Auth(temp.get('token'))
			print(auth.auth())

		insert_contact_pattern = re.compile(r'/insert-contact$')
		if(re.search(insert_contact_pattern, path)):
			contact = contacts(
				contact_name = temp.get('contact_name'),
				contact_phone_number = temp.get('contact_phone_number'),
				contact_email = temp.get('contact_email'),
				contact_address = temp.get('contact_address')
			)
			contact.insert(token = temp.get('token'))


	########
	#UPDATE#
	########
	#PUT method Defination
	def do_PUT(self):
		path = self.path
		if(path=='/'):
			self.wfile.write('Welcome to minapi'.encode())

		temp = self._set_headers()

		change_pass_pattern = re.compile(r'/change_pass$')
		if(re.search(change_pass_pattern, path)):
			user = users(temp)
			user.change_pass()

		update_contact_pattern = re.compile(r'/update_contact$')
		if(re.search(update_contact_pattern, path)):
			contact = contacts(
				contact_name = temp.get('contact_name'),
				contact_phone_number = temp.get('contact_phone_number'),
				contact_email = temp.get('contact_email'),
				contact_address = temp.get('contact_address')
			)
			contact.update(token = temp.get('token'))

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
			user = users(temp)
			user.delete()
