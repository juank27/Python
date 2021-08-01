import math
def run():
   my_dict = {}
   for i in range(1,101):
      if i % 3 != 0:
         my_dict[i] = i**3 #asigno i como llave y i**3 como value
   print(my_dict)
   #estructura
   #{key:value for value in iterable if condition}
   my_dict2 = {i:i**3 for i in range(1,101) if i % 3 != 0}
   print(my_dict2)
   
   #raiz de los primeros 1000 numeros
   my_dict3= {i:math.sqrt(i) for i in range (1,1001)}
   print(my_dict3)
if __name__ == "__main__":
   run()