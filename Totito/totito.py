from funcion_totito import ganador
lista = [[ 65, 66, 67], [68, 69, 70], [71, 72, 73]]
posicion_tomada = []

print ("Bienvenidos a Totito\n")

while ganador(lista) == 1 or ganador(lista) == -1 or ganador(lista) == False:

	print (chr(lista[0][0]), chr(lista[0][1]), chr(lista[0][2]))
	print (chr(lista[1][0]), chr(lista[1][1]), chr(lista[1][2]))
	print (chr(lista[2][0]), chr(lista[2][1]), chr(lista[2][2]))

		
	tiro = input(" Jugador 1, En que posicion quiere poner X: ")
	tiro_valor = ord(tiro)-65
	tiro_fila = tiro_valor % 3
	tiro_columna = tiro_valor //3

	if tiro_valor in posicion_tomada:
			print("Use otra posicion perdio el turno \n")
	else:
		posicion_tomada.append(tiro_valor)
		lista[tiro_columna][tiro_fila] = 88


	print (chr(lista[0][0]), chr(lista[0][1]), chr(lista[0][2]))
	print (chr(lista[1][0]), chr(lista[1][1]), chr(lista[1][2]))
	print (chr(lista[2][0]), chr(lista[2][1]), chr(lista[2][2]))

	tiro = input("Jugador 2, En que posicion quiere poner O: ")
	tiro_valor = ord(tiro)-65
	tiro_fila = tiro_valor % 3
	tiro_columna = tiro_valor //3

	if tiro_valor in posicion_tomada:
		print("Use otra posicion perdio el turno \n")
	else:
		posicion_tomada.append(tiro_valor)
		lista[tiro_columna][tiro_fila] = 79