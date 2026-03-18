# Datos del usuario
edad_usuario = 18
saldo_billetera = 55.0
tiene_suscripcion_premium = True

# Precio del juego
precio_juego = 60

# Cálculo del precio final usando operadores
precio_final = precio_juego - (precio_juego * 0.10 * tiene_suscripcion_premium)

# Evaluación de la compra
compra_exitosa = edad_usuario >= 17 and saldo_billetera >= precio_final

print("Precio final:", precio_final)
print("¿Compra exitosa?", compra_exitosa)