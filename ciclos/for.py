# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

contador = 1
print(contador)
while contador < 1000:
    # contador = contador + 1 -> es exactamente igual a la línea de abajo
    contador += 1
    print(contador)

for contador in range(1000):
    print(contador)