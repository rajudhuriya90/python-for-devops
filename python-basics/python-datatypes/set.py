# Set storing unique services
services = {"nginx", "docker", "ssh", "nginx"}

print("Services:", services)

print("Total Unique Services:", len(services))



############## this program for the practice#####
cpu_usage = 75
memory_usage = 68
disk_usage = 85

average = (cpu_usage + memory_usage + disk_usage) // 3

print("CPU Usage:", cpu_usage)
print("Memory Usage:", memory_usage)
print("Disk Usage:", disk_usage)

print("Average Usage:", average)

if average > 80:
    print("Server Status: Critical")
elif average > 60:
    print("Server Status: Moderate Load")
else:
    print("Server Status: Healthy")