from collections import deque
def es_palindromo(palabra):
	pila = []
	cola = deque([])
	palindromo = (" ")
	for letra in palabra:
		pila.append(letra) # Pop
		cola.append(letra) # popleft
	for i in range(len(palabra)):
		if cola.popleft() != pila.pop():
			return False
	return True



nombre = ("ana")
print (es_palindromo(nombre))
