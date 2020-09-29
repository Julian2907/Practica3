n = input(input())
x = 1
y = 0
xy = 0
for i in range(1, n+1):
    if i % 3 == 0:
        z = x + y
        x = y
        y = z
        print(z, end=" ")
    else:
        print(0, end=" ")
#Julian Andres Sanchez Apaza