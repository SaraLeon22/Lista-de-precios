import math

#Crear variables

Datos_Usuario = []

#Pedir datos al usuario
    
for i in range (10):
    while True:
        try:
            Lista = float(input("Ingresa el valor de tus compras, por favor: "))
            Datos_Usuario.append(Lista)
            break
        except ValueError:
            print("Por favor ingrese un numero valido.")
        

#Organizar datos dados por el usuario

print(f'Estos son los datos proporcionados: {Datos_Usuario}\t\t')

#Calcular el precio final

Total = sum(Datos_Usuario)

#Calcular el promedio

Promedio = Total/ len(Datos_Usuario)

#Dar datos finales

print(f'Este es tu resultado final:\t Total: {Total}\t Promedio: {Promedio}\t')
