import os
os.system('cls')
#con parámetro
def saludo(nombre):
    print('Holi, ', nombre)
def suma(a,b):
    sum = a + b
    print(str(a) + " + " + str(b) + " es igual a " + str(sum))

#main
nombre = "Daru"
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
saludo(nombre)
suma(num1,num2)