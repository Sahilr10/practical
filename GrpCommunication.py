#Server

import socket
import threading

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(5)

clients = []

print('Server is listening on port 9999...')

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)
                client.close()

def receive():
    while True:
        client, address = server.accept()
        print(f'Connection from {address} has been established.')
        clients.append(client)
        thread =  threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()

#Client

import socket
import threading

client = socket.socket()
client.connect(('localhost', 9999))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print('Connection closed by the server.')
            break

def send():
    while True:
        message = input()
        client.send(message.encode())

threading.Thread(target=receive).start()
threading.Thread(target=send).start()  