# Python Variables Example
# Demonstrates different variable types used in DevOps scripting

# String variables
server_name = "web-server-01"
environment = "production"

# Integer variables
cpu_cores = 4
running_containers = 6

# Float variable
cpu_load = 2.75

# Boolean variable
server_active = True

# List variable
services = ["nginx", "docker", "ssh"]

# Dictionary variable
server_info = {
    "ip": "192.168.1.10",
    "os": "Ubuntu",
    "region": "Mumbai"
}

# Printing variables
print("Server Name:", server_name)
print("Environment:", environment)
print("CPU Cores:", cpu_cores)
print("Running Containers:", running_containers)
print("CPU Load:", cpu_load)
print("Server Active:", server_active)

print("\nServices Running:")
print(services)

print("\nServer Information:")
print(server_info)

# Variable calculation
total_resources = cpu_cores + running_containers
print("\nTotal Resource Count:", total_resources)