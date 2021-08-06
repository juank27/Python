def main():
   a = 1
   def nested(): #funcion anidada que solo pertenece a main
      print(a)
   nested() #para poder ser utilizada debe ser retornada.
   return nested

my_func = main()
my_func() #realiza el contenido de nested    

del(main) #elimina la funcion 
my_func() #utilidad del closure recordando la funcion
