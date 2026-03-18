#Función menu:Imprime un menu de opciones y retorna la 
#Opción elegida por el ususario
def menu():
    #No se debe permitir una opcion que no está
    opcion=0
    while opcion<1 or opcion > 4 :
        print("1.suma\n2. Resta\n3. Multiplicacion\n4. Division")
        opcion=int(input("selecciones una opción:"))
    return opcion

operacion=menu()
print(f"El usuario eligió  la opción {operacion}")
if operacion == 1:
    pass
elif operacion == 2:
    pass
elif operacion == 3:
    pass