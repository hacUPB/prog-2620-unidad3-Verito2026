'''
### Ejercicio 1: Conversor de Temperatura

**Dificultad:** Principiante

Crea un programa que convierta temperaturas entre Celsius y Fahrenheit. El programa debe:

1. Preguntar al usuario si desea convertir de Celsius a Fahrenheit (ingresando 'C') o de Fahrenheit a Celsius (ingresando 'F')
2. Aceptar un valor de temperatura como entrada
3. Realizar la conversión usando la fórmula apropiada
4. Continuar pidiendo conversiones hasta que el usuario ingrese 'Q' para salir

**Entrada:** Un carácter ('C', 'F', o 'Q') y un valor numérico de temperatura
**Salida:** El valor de temperatura convertido con las unidades correspondientes
'''
while True:
    celsius_o_farenheit=input("Si desea convertir de celsius a farenheit, ingrese 'c' ; si desea convertirr de farenheit a celsius ingrese 'f'")
    if celsius_o_farenheit=="q":
        break
    temperatura=float(input("Ingrese la temperatura, sin unidad de medida"))
    if celsius_o_farenheit == "c":
        conversion=(temperatura*1.8)+32
        print(f"{temperatura}c en farenheit es:{conversion}")
    elif celsius_o_farenheit=="f":
        conversion=(temperatura-32)/1.8
        print(f"{temperatura}f en celsius es:{conversion}")
    else:
        print("Opcion no valida")
    
