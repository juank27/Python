#ley de la multiplicacion
#crecimiento exponencial
def f(n):
   for i in range(n):
      for j in range(n):
         print(i,j)
# O(n) * O(n) = O(n*n) = O(n²) 

#Ley de la suma
#crecimiento lineal
def f(n):
   for i in range(n):
      print(i)

   for i in range(n):
      print(i)
#O(n) + O(n) = O(n+n) = O(2n) = O(n) // Crecimiento lineal

#recursividad
def fibonacci(n):
   if n == 0 or n == 1:
      return 1
   return fibonacci(n - 1) + fibonacci(n - 2)
#O(2**n) // tiene varias llamadas recursivas y eso hace al algoritmo con un crecimiento exponencia
