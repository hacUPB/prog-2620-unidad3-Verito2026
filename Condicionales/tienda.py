'''
Una tienda ofrece una promoción, por la compra de 3 articulos, el costo del elemento de menor valor tiene un descuento del 50%
'''
articulo_1= int(input("Ingrese el valor del primer artículo")) 
articulo_2= int(input("Ingrese el valor del segundo artículo"))
articulo_3= int(input("Ingrese el valor del tercer artículo"))
total= articulo_1 + articulo_2 + articulo_3

if articulo_1 < articulo_2:
    menor = articulo_1
else:
    menor = articulo_2
if menor < articulo_3:
    definitivo=menor
else:
    definitivo=articulo_3
total= total-(definitivo*0.5)
print(f"El valor a pagar es ${total}")