pesos = input("¿Cuántos pesos colombianos tienes? ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")

dolares = input("¿Cuántos dólares tienes? ")
dolares = float(dolares)
valor_peso = 0.00027
pesos = dolares / valor_peso
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")