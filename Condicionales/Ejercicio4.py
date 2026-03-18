'''
El Ministerio de Salud clasifica las personas según las etapas del ciclo de vida, con el fin de tener una idea sobre su vulnerabilidad. Diseñe un algoritmo que pida al usuario su edad y la clasifique según la etapa del ciclo de vida que le corresponda. Verifique que el usuario no ingrese valores menores a cero. Clasificación etaria de la población colombiana:

- Infancia [0-6) años)
- Niñez [6 - 12) años)
- Adolescencia (12 - 20 años)
- Juventud (20 - 25 años)
- Adultez (25- 60 años)
- Ancianidad / Vejez (60 años o más)
'''
edad=float(input("Ingrese su edad:"))
if 0<=edad<6:
    print("Usted está en la infancia")
elif 6<=edad<12:
    print("Usted está en la niñez")
elif 12<=edad<20:
    print("Usted está en la adolescencia")
elif 20<=edad<25:
    print("Usted está en la juventud")
elif 25<=edad<60:
    print("Usted está en la adultez")
elif 60<=edad:
    print("Usted está en la vejez")
print("Gracias por participar")
