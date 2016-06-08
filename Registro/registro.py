from validar import validar_nota
estudiantes = {

}
continuar = int(input("1. Crear Estudiante \n 2. Ingresar Notas \n 3. Reporte de notas \n 4. Salir \n "))
while continuar <= 3:
	if continuar == 1:
		nombre = input("Nombre del alumno: ")
		estudiantes[nombre] = []
		continuar = int(input("1. Crear Estudiante \n 2. Ingresar Notas \n 3. Reporte de notas \n 4. Salir \n "))
	elif continuar == 2:
		print(estudiantes)
		nombre = input("¿De que estudiante desea ingresar notas?")
		continuar2 = "si"
		while continuar2 == "si":
			estudiantes[nombre].append((nota = (int(input("Ingrese la nota: ")))))
			
			continuar2 = (input("quiere ingresar otra nota? si/no")
	elif continuar == 3:
		print(estudiantes)
		nombre = input("De que estudiante desea revisar su promedio?")
