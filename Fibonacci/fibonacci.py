def fibonacci(n):
	#Caso Base
	if n == 0:
		return 0
	#Caso Recursivo
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
