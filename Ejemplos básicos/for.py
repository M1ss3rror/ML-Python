import os
os.system('cls')
contador = 0 
for i in range(10000):
    if i % 333 == 0 and i % 5 == 0:
        contador = contador + 1
        print(i)
print (contador)