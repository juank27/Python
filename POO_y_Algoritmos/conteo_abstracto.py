#Conteo de pasos
def f(x):
   respuesta = 0 # 1 
   
   for i in range(1000): # 1000
      respuesta+=1
   
   for i in range(x): # x
      respuesta += x
   
   for i in range(x):   # x  ---> x * x = x²
      for j in range(x):# x  /
         respuesta += 1 # 1 ---> 1 + 1 = 2
         respuesta += 1 # 1 /
   
   return respuesta # 1

### Unificand todos los valores  genrea la ecuacion ###
##  1002 + x + 2x² ##