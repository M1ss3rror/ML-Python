#La empresa “Margarita” vende papas fritas de 7 referencias distintas. Se necesita conocer las
#ventas por referencia en un día y el total general de ventas, tanto en cantidades como en dinero

#Vector para cantidades(7)
#Vector referencia en dinero(7)
#Vector para totales(7)
#Ciclos
#Tgv
#Tgc

#declarar vector
cant, ref, total = [],[],[]
T = 7
def inicializar():
    for i in range(T):
        cant.append(0)
        ref.append(0)
        total.append(0)
    print(cant)

def captura():
    for i in range (T):
        cant[i] = int(input("Ingrese la cantidad de papas "))
    return cant

def referencias():
    for i in range(T):
        ref[i] = int(input("Ingrese el valor de las papas "))
    return ref

def costos(cant,ref):
    for i in range(T):
        total[i] = cant[i]*ref[i]
    return total

def mostrar(cant,ref,total):
    tgc = 0
    tgv = 0
    print(cant)
    print(ref)
    print(total)
    for i in range(T):
        tgc = tgc + cant[i]
    for i in range(T):
        tgv = tgv + total[i]
    print("Las ventas totales en unidades es de: ", tgc)
    print("Las ventas totales en dinero es de: ", tgv)

def titulo():
    print("Empresa Margarita")

def salir():
    print("Adiós...")

def main():
    titulo()
    inicializar()
    cant = captura()
    ref = referencias()
    total = costos(cant,ref)
    mostrar(cant,ref,total)
    salir()
    
#Bloque principal
main()