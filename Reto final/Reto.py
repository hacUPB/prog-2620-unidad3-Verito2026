consumo_base = 3 #en kg/km
factor_headwind = 1.18
factor_tailwind = 0.88
factor_neutro = 1
reserva_legal = 1200 #en kg

def combustible_tramo(distancia, viento):
    if viento == "headwind":
        factor = factor_headwind
    elif viento == "tailwind":
        factor = factor_tailwind
    else:
        factor = factor_neutro
    
    consumo = distancia * (consumo_base * factor)
    return consumo 


combustible_inicial = float(input("ingresar combustible inicial: "))
numero_tramos = int(input("Ingresa el número de tramos: "))
combustible_actual = combustible_inicial 
destino_final = input("Ingresa tu lugar de destino final: ")

for i in range(1, numero_tramos + 1 ):
    print(f"\nTramo {i}")

    distancia = float(input("Ingresa la distancia del tramo (en km): ")) #se pide ingresar la distancia del tramo
    viento = input("selecciona el tipo de viento (headwind,tailwind o neutro): ") #se pide ingresar el tipo de viento

    consumo = combustible_tramo(distancia,viento) #se llama a la funcion
    combustible_actual = combustible_actual - consumo 
    print(f"El consumo es: {consumo} kg")
    print(f"El combustible restante es: {combustible_actual} kg")

    if combustible_actual <= reserva_legal:
        print("ALERTA: Combustible en reserva")
        print("Andate a el aeropuesto más cercano")
        break #Ayuda de la IA para la implementacion el break
    else:
        print("Vuelo completado con exito")


if combustible_actual >= reserva_legal:
    print(f"Has llegado a {destino_final} sin utilizar el combustible de reserva, buen trabajo")




    



