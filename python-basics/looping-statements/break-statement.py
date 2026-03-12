## Example 1
for i in range(1, 10):
    if i == 5:
        break
    print(i)

## Example 2
i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1


## Example 3
services = ["nginx", "docker", "mysql"]

for service in services:
    if service == "docker":
        break
    print(service)

## Example 4
for i in range(10):
    if i == 3:
        break
    print("Number:", i)



## Example 5

x = 0

while True:
    print(x)
    if x == 2:
        break
    x += 1