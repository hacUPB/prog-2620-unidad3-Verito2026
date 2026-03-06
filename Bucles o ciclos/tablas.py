#Tabla de multiplicar
numero = int(input("Ingrese el numero:"))

for i in range(1,11,1):
    print(f"{numero} * {i} = {numero*i}")

#Ejercicio imprima hola 10 veces
for i in range(10):
    print("Hola")

#Ejercicio, que el usuario ingrese diez valores
print ("Ingrese 10 valores:")
for i in range(10):
    valor = int(input(f"Ingrese el valor {i+1}:"))