# List of servers
servers = ["S1", "S2", "S3"]

# Index to track next server
index = 0

def get_server():
    global index
    server = servers[index]
    index = (index + 1) % len(servers)
    return server


# Simulate incoming requests
requests = ["Req1", "Req2", "Req3", "Req4", "Req5"]

for req in requests:
    assigned_server = get_server()
    print(f"{req} → handled by {assigned_server}")