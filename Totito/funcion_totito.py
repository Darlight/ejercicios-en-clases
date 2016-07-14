def ganador(totito):
	suma = []
	for fila in totito:
		suma.append(sum(fila))
	for columna in range(3):
		suma.append(totito[0][columna]+totito[1][columna]+[2][columna])
	sumad1 = 0
	sumad2 = 0
	for diagonal in range(3):
		sumad1 += totito[diagonal][diagonal]
		sumad2 += totito[diagonal][2-diagonal]
		suma.append(sumad1)
		suma.append(sumad2)
	if 3 in suma:
		return 1
	elif -3 in suma:
		return -1
	else:
		return False 


def print_totito(totito):
	resultado = " "
	for i in range(3):
		for j in range(3):
			celda = totito(i)(j)
			if celda == 1:
				return "X"
			elif celda == -1:
				return "O"
			else:
				chr((3*i)+j+65)
