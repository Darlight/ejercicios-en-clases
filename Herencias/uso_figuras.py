from cuadrado import Cuadrado
from triangulo import Triangulo

desea_continuar = False
while desea_continuar == False:
	respuesta = int(input("1. Crear Figura \n 2. Salir "))
	if respuesta == 1:
		figura = int(input("1. Cuadrado \n 2. Triangulo "))
		if figura == 1:
			lado = int(input("Valor de los lados: "))
			cuadrado = Cuadrado(lado)
			respuesta_2 = int(input("1. Calcular el area \n 2. Imprimir figura "))
			if respuesta_2 == 1:
				print ("Area: ", cuadrado.calcular_area())
			elif respuesta_2 == 2:
				print ("Figura:" )
				print(cuadrado.imprimir())
		if figura == 2:
			base = int(input("Valor de base: "))
			altura = int(input("Valor de altura: "))
			triangulo = Triangulo(base,altura)
			respuesta_2 = int(input("1. Calcular el area \n 2. Imprimir figura "))
			if respuesta_2 == 1:
				print ("Area: ", triangulo.calcular_area())
			elif respuesta_2 == 2:
				print ("Figura:" )
				print(triangulo.imprimir())
	else: 
		desea_continuar = True
print("Gracias por el servicio usado")