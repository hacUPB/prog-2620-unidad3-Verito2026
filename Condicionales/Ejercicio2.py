'''
Un almacén cobra `$9 000` por costos de envío, pero ofrece el envío a domicilio gratis para compras superiores a `$100 000`. En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.
''' 

domicilio=9000
compra=float(input("Ingrese el valor de compra:"))
if compra > 100000:
    total= compra
    print(f"El total a pagar es:{total}")
else:
    total= compra + domicilio
    print(f"El total a pagar es:{total}")
print("Gracias por su compra, vuelva pronto")