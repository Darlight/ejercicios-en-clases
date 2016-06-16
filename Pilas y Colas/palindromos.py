from collections import deque
def es_palindromo(palabra):
	pila = []
	cola = deque([])
	for letra in palabra:
		pila.append(letra) # Pop
		cola.append(letra) # popleft
		if pila.pop() == cola.popleft():
			return True
		else:
			return False
