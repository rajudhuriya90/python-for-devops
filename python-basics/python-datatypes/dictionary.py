# Dictionary storing server information
server = {
    "name": "web-server",
    "ip": "192.168.1.10",
    "os": "Ubuntu",
    "region": "Mumbai"
}

print("Server Name:", server["name"])
print("IP Address:", server["ip"])
print("Operating System:", server["os"])
print("Region:", server["region"])

### seconad program of the dictionary###

# Dictionary storing container status
containers = {
    "nginx": "running",
    "redis": "stopped",
    "mysql": "running"
}

for name, status in containers.items():
    print(name, ":", status)