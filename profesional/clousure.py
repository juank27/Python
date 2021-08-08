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

#reto
def make_division_by(n):
   """this closuere returns a fuction that returns the division 
      of an x number by n
      """
   def division(x):
      return x/n
   return division
print("######### Reto ##########")
division_by_3 = make_division_by(3)
print(division_by_3(18))

division_by_5 = make_division_by(5)
print(division_by_5(100))

division_by_18 = make_division_by(18)
print(division_by_18(54))