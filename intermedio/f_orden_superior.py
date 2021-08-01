#funciones de orden superior
def saludo(func):
   func()

def hola():
   print("Hola!!")

def adios():
   print("Adios!!")

saludo(hola)
saludo(adios)

# uso con filter
my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 !=0, my_list))
print(odd)

#uso con map
my_list2 = [1,2,3,4,5,6]
squares = list(map(lambda x: x **2,my_list2))
print(squares)

#uso con reduce
from functools import reduce
my_list3 = [2,2,2,2,2]
all_miltiplied = reduce(lambda a, b : a * b, my_list3)
print(my_list3)