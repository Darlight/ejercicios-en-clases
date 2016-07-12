from funcion_totito.py import conseguir_ganador
from random import random
lista = [[ "A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"] ]]

print ("Bienvenidos a Totito")

jugador_1 = input("Jugador 1 Ingrese su nombre: ")
jugador_2 = input("Jugador 2 Ingrese su nombre: ")

print(lista[0])
print(lista[1])
print(lista[2])

tiro = input("En que posicion quiere ponerlo: ")
tiro_valor = ord(tiro)-65
tiro_fila = tiro_valor % 3
tiro_columna = tiro_valor //3

while conseguir_ganador:
	tiro = input("En que posicion quiere poner X: ")
	tiro_valor = ord(tiro)-65
	tiro_fila = tiro_valor % 3
	tiro_columna = tiro_valor //3

	lista[tiro_columna][tiro_fila] = chr(88)
	print(lista[0])
	print(lista[1])
	print(lista[2])

	tiro = input("En que posicion quiere poner X: ")
	tiro_valor = ord(tiro)-65
	tiro_fila = tiro_valor % 3
	tiro_columna = tiro_valor //3

	lista[tiro_columna][tiro_fila] = chr()
	print(lista[0])
	print(lista[1])
	print(lista[2])








	

