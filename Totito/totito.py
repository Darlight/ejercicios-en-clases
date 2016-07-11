from random import random
lista = [ [chr(65), chr(66), chr(67)], [chr(68), chr(69), chr(70)], [chr(71), chr(72), chr(73)] ]
print ("Bienvenidos a Totito")

jugador_1 = input("Jugador 1 Ingrese su nombre: ")
jugador_2 = input("Jugador 2 Ingrese su nombre: ")

print(lista[0])
print(lista[1])
print(lista[2])

print(jugador_1, "Usted usa X")
print(jugador_2, "Usted usa O")

ubicacion_x = input("\nQue lugar quieres poner X: ")
ubicacion_o = input("\nQue lugar quieres poner O: ")

if ubicacion_x == lista[0][0]:
	lista[0][0] = "X"
elif ubicacion_x == lista[0][1]:
	lista[0][1] = "X"
elif ubicacion_x == lista[0][2]:
	lista[0][2] = "X"
elif ubicacion_x == lista[1][0]:
	lista[1][0] = "X"
elif ubicacion_x == lista[1][1]:
	lista[1][1] = "X"
elif ubicacion_x == lista[1][2]:
	lista[1][2] = "X"
elif ubicacion_x == lista[2][0]:
	lista[2][0] = "X"
elif ubicacion_x == lista[2][1]:
	lista[2][1] = "X"
elif ubicacion_x == lista[2][2]:
	lista[2][2] = "X"

if ubicacion_o == lista[0][0]:
	lista[0][0] = "O"
elif ubicacion_o == lista[0][1]:
	lista[0][1] = "O"
elif ubicacion_o == lista[0][2]:
	lista[0][2] = "O"
elif ubicacion_o == lista[1][0]:
	lista[1][0] = "O"
elif ubicacion_o == lista[1][1]:
	lista[1][1] = "O"
elif ubicacion_o == lista[1][2]:
	lista[1][2] = "O"
elif ubicacion_o == lista[2][0]:
	lista[2][0] = "O"
elif ubicacion_o == lista[2][1]:
	lista[2][1] = "O"
elif ubicacion_o == lista[2][2]:
	lista[2][2] = "O"

print(lista[0])
print(lista[1])
print(lista[2])