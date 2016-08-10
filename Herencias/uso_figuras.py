from cuadrado import Cuadrado
from jesus import FiguraGeometrica
from triangulo import Triangulo

desea_continuar = False
while desea_continuar == False:
	respuesta = int(input("1. Crear Figura \n 2. Salir"))
	if respuesta == 1:
		figura = int(input("1. Cuadrado \n 2. Triangulo"))
		if figura == 1:
			lados = int(input("Valor de los lados: "))
			respuesta_2 = int(input("1. Calcular el area \n 2. Imprimir figura"))
			if respuesta_2 == 1:
				print ("Area: ",lados.calcular_area())
			elif respuesta_2 == 2:
				print ("Figura: " ,lados.imprimit())


	else: 
		desea_continuar = True
print("Gracias por el servicio usado")