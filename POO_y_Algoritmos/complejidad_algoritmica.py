import time
#no es bueno medir con el tiempo ya que a medida que incrementa el valor no se puede predecir

#factorial normal
def factorial(n):
   respuesta = 1
   
   while n > 1 :
      respuesta *= n
      n -= 1 
   return respuesta

#Metodo factorial recursivo 
def factorial_r(n):
   if n == 1:
      return 1
   return n * factorial(n - 1)

if __name__ == '__main__':
   n = 200000
   
   comienzo = time.time()
   factorial(n)
   finaal = time.time()
   print(finaal - comienzo)
   
   comienzo = time.time()
   factorial_r(n)
   finaal = time.time()
   print(finaal - comienzo)