#creando un iterador
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

#iterando un iterador
#print(next(my_iter))
#cuando no quedan datos, la excepcion StopIteration es elevada
#iterando con un while y forma correcta de hacerlo
while True:
   try:
      element = next(my_iter)
      print(element)
   except StopIteration:
      break

#Forma bonita de hacerlo
for element in my_list:
   print(element)