from jesus import FiguraGeometrica

class Triangulo(FiguraGeometrica):

	def __init__(self, base, altura):
		super().__init__(base,altura)

	def imprimir(self):
		resultado = " "

		for i in range(self.altura):
			resultado += "*" + (i + 1) * "\n"
			return resultado

	def calcular_area(self):
		return super().calcular.area()/ 2.0