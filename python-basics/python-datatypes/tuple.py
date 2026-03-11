# Tuple storing server ports
ports = (22, 80, 443, 3306)

print("Server Ports:", ports)

print("First Port:", ports[0])
print("Total Ports:", len(ports))



####second program show tuple used ####


# Tuple storing service names
services = ("nginx", "docker", "ssh")

print("Running Services:")

for service in services:
    print(service)