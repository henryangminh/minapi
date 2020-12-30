from http.server import BaseHTTPRequestHandler
import json
import re
from src.Model import users
from src.Database import Database
# from urllib.parse import unquote
from src.utils.json_utils import to_dict

#open json file and give it to data variable as a dictionary
with open("db.json") as data_file:
	data = json.load(data_file)

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
		#prints all the keys and values of the json file\
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

		# else:
		# 	# query = urlparse(self.path).query
		# 	# query_components = dict(qc.split('=') for qc in query.split("&"))
		# 	path = self.path
		# 	path = path.split('/')[1:]
		# 	self.wfile.write(json.dumps(path).encode())

	######
	#VIEW#
	######
	#VIEW method defination
	def do_VIEW(self):
		#dict var. for pretty print
		display = {}
		temp = self._set_headers()
		#check if the key is present in the dictionary
		if temp in data:
			display[temp] = data[temp]
			#print the keys required from the json file
			self.wfile.write(json.dumps(display).encode())
		else:
			error = "NOT FOUND!"
			self.wfile.write(bytes(error,'utf-8'))
			self.send_response(404)

    ########
    #CREATE#
    ########
    #POST method defination
	def do_POST(self):
		# temp = self._set_headers()
		# key=0
		# #getting key and value of the data dictionary
		# for key,value in data.items():
		# 	pass
		# index = int(key)+1
		# data[str(index)]=str(temp)
		# #write the changes to the json file
		# with open("db.json",'w+') as file_data:
		# 	json.dump(data,file_data)
		# #self.wfile.write(json.dumps(data[str(index)]).encode())
		path = self.path
		if(path=='/'):
			self.wfile.write('Welcome to minapi'.encode())

		temp = self._set_headers()
		temp = to_dict(temp)

		user_pattern = re.compile(r'/register$')
		if(re.search(user_pattern, path)):
			print(temp)
			# self.wfile.write(temp.encode())


	########
	#UPDATE#
	########
	#PUT method Defination
	def do_PUT(self):
		temp = self._set_headers()
		#seprating input into key and value
		x = temp[:1]
		y = temp[2:]
		#check if key is in data
		if x in data:
			data[x] = y
			#write the changes to file
			with open("db.json",'w+') as file_data:
				json.dump(data,file_data)
			#self.wfile.write(json.dumps(data[str(x)]).encode())
		else:
			error = "NOT FOUND!"
			self.wfile.write(bytes(error,'utf-8'))
			self.send_response(404)

	########
	#DELETE#
	########
	#DELETE method defination
	def do_DELETE(self):
		temp = self._set_headers()
		self.wfile.write(temp.encode())
		#check if the key is present in the dictionary
		if temp in data:
			del data[temp]
			#write the changes to json file
			with open("db.json",'w+') as file_data:
				json.dump(data,file_data)
		else:
			error = "NOT FOUND!"
			self.wfile.write(bytes(error,'utf-8'))
			self.send_response(404)
