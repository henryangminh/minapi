import os
from http.server import HTTPServer
from ServiceHandler import ServiceHandler

#Server Initialization
if __name__ == "__main__":
    PORT = int(os.environ['PORT'])
    # PORT = 8080

    try:
        serverAdd = ('', PORT)
        print(f'Started httpserver on port {PORT}')
        server = HTTPServer(serverAdd, ServiceHandler)
        server.serve_forever()


    except KeyboardInterrupt:
        print ('CTRL + C RECEIVED - Shutting down the REST server')
        server.socket.close()
