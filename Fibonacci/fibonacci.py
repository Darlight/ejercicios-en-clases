def fibonacci(n):
	#Caso Base
	if n <= 1:
		return 1
	#Caso Recursivo
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
