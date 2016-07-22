import random
from palabras import lista_de_palabras
print ("Bienvenido al Ahorcado")

palabra_elegida = random.choice(lista_de_palabras)
print (palabra_elegida)
oportunidades = 0
ganador = False
# usar "letra" in "palabra" para que el juego funcione.
# crear el el stickman con: "O", "I", "/", "\" y el palo.
while oportunidades != 7:
	for espacios in len(palabra_elegida):
		print("_")


