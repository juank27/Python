def make_multiplier(x):
   def multiplier(n):
      return x * n
   return multiplier

#toman el valor de la x
times10 = make_multiplier(10)
times4 = make_multiplier(4)
n = times10(times4(2))
#ahora con el valor de la x recordado toman el de la n
print(times10(3))
print(times4(5))
print(times10(times4(2)))
print(n)

#Multiplicar un string por un numero
def palabra(string:str):
   assert type(string) == str, "Se deben utilizar cadenas "
   def multiplicador(n : int):
      return string * n
   return multiplicador

name = palabra("Juan")
numero = name(3)
print(numero)