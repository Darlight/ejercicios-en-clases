from random import random
lista = [[ "A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"] ]
posicion_tomada = []

print ("Bienvenidos a Totito")
b = 4
while b != 5:
	print(lista[0])
	print(lista[1])
	print(lista[2])
		
	tiro = input(" Jugador 1, En que posicion quiere poner X: ")
	tiro_valor = ord(tiro)-65
	tiro_fila = tiro_valor % 3
	tiro_columna = tiro_valor //3

	if tiro_valor in posicion_tomada:
			print("Use otra posicion perdio el turno \n")
	else:
		posicion_tomada.append(tiro_valor)
		lista[tiro_columna][tiro_fila] = chr(88)

	print(lista[0])
	print(lista[1])
	print(lista[2])

	tiro = input("Jugador 2, En que posicion quiere poner O: ")
	tiro_valor = ord(tiro)-65
	tiro_fila = tiro_valor % 3
	tiro_columna = tiro_valor //3

	if tiro_valor in posicion_tomada:
			print("Use otra posicion perdio el turno \n")
	else:
		posicion_tomada.append(tiro_valor)
		lista[tiro_columna][tiro_fila] = chr(79)
