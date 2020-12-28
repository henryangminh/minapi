import os
from http.server import HTTPServer
from ServiceHandler import ServiceHandler

# DATABASE_URL = os.environ.get('DATABASE_URL')

#Server Initialization
if __name__ == "__main__":
    # PORT=int(os.environ['PORT'])

    try:
        # serverAdd = ('', PORT)
        serverAdd = ('', 8080)
        # print(f'Started httpserver on port {PORT}')
        server = HTTPServer(serverAdd, ServiceHandler)
        server.serve_forever()


    except KeyboardInterrupt:
        print ('CTRL + C RECEIVED - Shutting down the REST server')
        server.socket.close()