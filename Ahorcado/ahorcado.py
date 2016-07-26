import random
from palabras import lista_de_palabras
from funciones import letra_en_palabra
print ("Bienvenido al Ahorcado \n")

palabra_elegida = random.choice(lista_de_palabras)
oportunidades = 0
ganador = False
letras_separadas = list(palabra_elegida)
error = False
# usar "letra" in "palabra" para que el juego funcione.
# crear el stickman con: "O", "I", "/", "\" y el palo.
for guion in range(len(letras_separadas)):
	letras_separadas[guion] = "_"
while oportunidades != 7 or ganador == True:
	estado = False
	print(letras_separadas)

	letra_ingresada = input("Ingrese la letra deseada: ")
	if letra_ingresada in palabra_elegida:
		for i in range(len(palabra_elegida)):
			if palabra_elegida[i] == letra_ingresada:
				letras_separadas[i] = letra_ingresada
	else:
		oportunidades = oportunidades + 1
		error = True
		dibujo(error)






