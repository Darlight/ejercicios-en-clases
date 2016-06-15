def suma(lista):
	# Caso Base
	if len(lista) == 1:
		return lista[0]

	# Caso Recursivo
	return lista[0] + suma(lista[1:])
	 
numeros = [12,33,40,52]
print(suma(numeros))

