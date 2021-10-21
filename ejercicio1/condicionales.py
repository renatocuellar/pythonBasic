edad = int(input("Escribe tu edad: "))
diferencia = edad - 18
diferencia = str(diferencia)

if edad >= 18:
    print("Eres mayor de edad hace " + diferencia + " años")
else:
    print("Aún eres menor de edad")