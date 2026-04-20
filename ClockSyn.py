# Server

import socket
import time

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(5)

clients = []
times = []

print('Server is running...')

for i in range(3):
    client, addr = server.accept()
    print(f'Client {addr} connected')
    clients.append(client)

for client in clients:
    t = float(client.recv(1024).decode())
    times.append(t)

server_time = time.time()
times.append(server_time)

average_time = sum(times) / len(times)

for i, client in enumerate(clients):
    offset = average_time - times[i]
    client.send(str(offset).encode())
    print(f'Sent offset {offset} to client {i}')

print('Clock synchronization complete.')
server.close()

# Client
import socket
import time

client = socket.socket()
client.connect(("localhost", 6000))

# Send current time
local_time = time.time()
client.send(str(local_time).encode())

# Receive adjustment
diff = float(client.recv(1024).decode())

# Adjust clock
new_time = local_time + diff

print("Old Time:", local_time)
print("Adjusted Time:", new_time)

client.close()