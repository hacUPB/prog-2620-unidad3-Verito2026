#Genera una constante de texto que será la contraseña.Luego pida al usuario que ingrese la contraseña.Mientras la contraseña no sea la correcta, debe continuar a pedir la contraseña. Si esta es correcta, se deja continuar al resto del programa.

password = "verito1208"
p = input("Ingrese la contraseña:")

while password != p:  
    print("Contraseña incorrecta")  
    p = input("Ingrese la contraseña:") 

print("Acceso concedido")
   

