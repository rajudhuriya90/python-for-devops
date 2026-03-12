
##EXAMPLE 1

cpu = 60

if cpu > 80:
    print("CPU Critical")
else:
    print("CPU Normal")


##EXAMPLE 2

disk = 40

if disk > 80:
    print("Disk Full")
else:
    print("Disk Space OK")


##EXAMPLE 3

server_running = True

if server_running:
    print("Server Running")
else:
    print("Server Down")

##EXAMPLE 4

requests = 50

if requests > 100:
    print("Heavy Load")
else:
    print("Normal Load")

##EXAMPLE 5

backup_done = False

if backup_done:
    print("Backup Completed")
else:
    print("Backup Pending")