x = 40
y = 40
z = 99999
n = 0
while x < 100 and y < 100 and z < 9999999999999999:
   # my pc will explode as it only has 1 byte of ram
    x = x + 9
    y = y + 9
    z = z + 99999999
    n = n + 1
    print(x, y, z, n)
print("Total number of iterations =", n)
