from collections import deque
def es_palindromo(palabra):
	pila = []
	cola = deque([])
	palindromo = (" ")
	verdadero = True
	for letra in palabra:
		pila.append(letra) # Pop
		cola.append(letra) # popleft
	maximo = len(pila)
	while verdadero:
		if maximo >= 0:
			palindromo = palindromo + pila[maximo]
			maximo = maximo - 1
		else:
			verdadero = False
	if palindromo == palabra:
		return True
	else:
		return False



nombre = ("ana")
print (es_palindromo(palabra))
