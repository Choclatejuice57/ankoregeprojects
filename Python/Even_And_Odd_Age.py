age = int(input("Enter Age"))

if (age % 2) == 0:
    start = 0
else:
    start = 1

while start <= age:
    print(start)
    start = start + 2
