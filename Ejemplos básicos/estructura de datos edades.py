import os
os.system('cls')
edades = [20,41,6,18,23]
#recorriendo los elementos
for edad  in edades:
    print("El valor de la lista en la posició", edad)

#recorriendo los indices
for i in range(len(edades)):
    print(edades[i])
#con while y los índices
indice = 0
while indice < len(edades):
    print(edades [indice])
    indice += 1
#trabajo con listas
numeros =[]
numeros.append(10)
numeros.append(5)
numeros.append(3)
print(numeros)
numeros.pop(1) #borra por indice
#mostrará 10 5 3
print(numeros)
numeros.remove(10) #borra por contenido
print(numeros)
