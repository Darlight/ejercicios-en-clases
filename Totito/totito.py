from funcion_totito import ganador, print_totito
lista = [[ ord("A"), ord("B"), ord("C")], [ord("D"), ord("E"), ord("F")], [ord("G"), ord("H"), ord("I")] ]

print ("Bienvenidos a Totito\n")
while ganador(lista):

	print(lista[0])
	print(lista[1])
	print(lista[2])
		
	tiro = input(" Jugador 1, En que posicion quiere poner X: ")
	tiro_valor = ord(tiro)-65
	tiro_fila = tiro_valor % 3
	tiro_columna = tiro_valor //3

	print(print_totito(lista))

	print(lista[0])
	print(lista[1])
	print(lista[2])

	tiro = input("Jugador 2, En que posicion quiere poner O: ")
	tiro_valor = ord(tiro)-65
	tiro_fila = tiro_valor % 3
	tiro_columna = tiro_valor //3