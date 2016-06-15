def maximo_numero(lista):
	#Caso Base
	if len(lista) == 1:
		return lista[0]
	#Procedimiento de menor a mayor
	sublista = (lista[1:])
	submaximo = maximo_numero(sublista)
	if lista[0] > submaximo:
		return lista[0]
	return submaximo


numeros = [12,344,54325,545,23,677,1534243]	
print(maximo_numero(numeros))