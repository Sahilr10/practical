# Server

from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y    

def subtract(x, y):
    return x - y

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(add, 'add')
server.register_function(subtract, 'subtract')

server.serve_forever()

# Client
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
print(proxy.add(5, 3))       # Output: 8
print(proxy.subtract(5, 3))  # Output: 2

