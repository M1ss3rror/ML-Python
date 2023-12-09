# Actividad 1 - Programa de Cambio de Divisas
# Proyecto de Grupo para Diplomado deMachine Learning con Python
# Grupo 15
#Integrantes: Laura Sofía Mora Gonzalez
            # Edwin Alexander Ospina Penna
            # Fiorella Natania Sánchez Rocha
            # Luis Carlos Ramirez Zuñiga
            # Luis Felipe Vasquez Acevedo
            # Dariana Gabriela Gomez Diaz

import os
os.system('cls')
#Tasa de cambio respecto al dolar americano
tasas_cambio = {
    ('EUR'): 0.92,
    ('GBP'): 0.79,
    ('USD'): 1,
    ('MXN'): 17.19,
    ('COP'): 4376.00,
    ('CAN'): 1.35
}
# Función para realizar el cambio de divisas
def cambiar_divisas(cantidad, divisa_origen, divisa_destino):
    if divisa_origen in tasas_cambio and divisa_destino in tasas_cambio:
        tasa_origen_a_usd = tasas_cambio[divisa_origen]
        tasa_destino_a_usd = tasas_cambio[divisa_destino]
        
        cantidad_usd = cantidad / tasa_origen_a_usd
        cantidad_destino = cantidad_usd * tasa_destino_a_usd
        
        ganancia_comprador = cantidad_destino - cantidad
        ganancia_vendedor = cantidad - cantidad_destino
        
        return cantidad_destino, ganancia_comprador, ganancia_vendedor
    else:
        return None  # Las tasas de cambio no están definidas

# Solicitar entrada al usuario
cantidad_a_cambiar = float(input("Ingrese la cantidad a cambiar: "))
divisa_origen = input("Ingrese la divisa de origen (EUR, USD, GBP, MXN, COP, CAN): ").upper()
divisa_destino = input("Ingrese la divisa de destino (EUR, USD, GBP, MXN, COP, CAN): ").upper()

# Validar entrada del usuario
if divisa_origen not in tasas_cambio or divisa_destino not in tasas_cambio:
    print('Las tasas de cambio no están definidas. Intente de Nuevo, seleccionando las opciones indicadas (:')
    print('¡Hasta pronto!')
else:
    resultado = cambiar_divisas(cantidad_a_cambiar, divisa_origen, divisa_destino)

    if resultado:
        cantidad_destino, ganancia_comprador, ganancia_vendedor = resultado
        print(f"{cantidad_a_cambiar:.2f} {divisa_origen} equivale a {cantidad_destino:.2f} {divisa_destino}")
        print(f"Ganancia para el comprador: {ganancia_comprador:.2f} {divisa_destino}")
        print(f"Ganancia para el vendedor: {ganancia_vendedor:.2f} {divisa_origen}")
    else:
        print("Tasas de cambio no definidas para la conversión especificada.")