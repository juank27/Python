def factorial(n):
   """Calcula el factorial de n
   n int > 0
   return n!
   """
   if  n == 1:
      return 1
   return n * factorial(n-1) 

print(factorial(0))


def fibonacci(n):
   if n == 0 or n == 1:
      return 1
   return fibonacci(n - 1) + fibonacci(n - 2)
