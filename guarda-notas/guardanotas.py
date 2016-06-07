notas = []
continuar = "si"
while continuar == "si":
	nota = int(input("Ingrese la nota: "))
	notas.append(nota)
	continuar = input("Desea continuar? si/no \n")

archivo = open("notasguardadas.txt","w")

for nota in notas:
	archivo.write(str(nota))
	archivo.write("\n")

archivo.close()