## EXAMPLE 1
disk = 75

if disk > 90:
    print("Disk Critical")
elif disk > 70:
    print("Disk Warning")
else:
    print("Disk Healthy")


## EXAMPLE 2
cpu = 85

if cpu > 90:
    print("CPU Critical")
elif cpu > 70:
    print("CPU Moderate")
else:
    print("CPU Normal")

## EXAMPLE 3
traffic = 300

if traffic > 500:
    print("Server Overload")
elif traffic > 200:
    print("Medium Traffic")
else:
    print("Low Traffic")


## EXAMPLE 4
memory = 60

if memory > 90:
    print("Memory Critical")
elif memory > 70:
    print("Memory Warning")
else:
    print("Memory Normal")

## EXAMPLE 5

temperature = 35

if temperature > 45:
    print("Server Overheating")
elif temperature > 30:
    print("Temperature Warm")
else:
    print("Temperature Normal")