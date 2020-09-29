a, b = map(int, input().split())
c = 0
p = 0
i = 0
for i in range(a+1, b,):
    print(1, end=" ")
    c = c + 1
    if 1 % 2 == 0:
        p = p + i
    else:
        i = i + i
print()
print("hay", c , "numeros")
print("la suma de los pares es: ", p)
print("la suma de los impares es ", i)
#Julian Andres Sanchez Apaza