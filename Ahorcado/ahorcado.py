import random
from palabras import lista_de_palabras
from funciones import letra_en_palabra
print ("Bienvenido al Ahorcado \n")

palabra_elegida = random.choice(lista_de_palabras)
oportunidades = 0
ganador = False
guiones = ("_ "*int(len(palabra_elegida)))
letras_separadas = list(palabra_elegida)
# usar "letra" in "palabra" para que el juego funcione.
# crear el stickman con: "O", "I", "/", "\" y el palo.
while oportunidades != 7:
	for guion in range(len(letras_separadas)):
		letras_separadas[guion] = "_ "

	print(letras_separadas)
	letra_ingresada = input("Ingrese la letra deseada: ")
	if letra_ingresada in letras_separadas:
		print("prueba")
		

	oportunidades = oportunidades + 1





