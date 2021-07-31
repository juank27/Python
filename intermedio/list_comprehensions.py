def listCuadrado():
   lista = []
   for i in range(0,100):
      if (i % 3) != 0:
         lista.append(i**2)
   print(lista)
   #list comprehensions que realiza lo mismo que el anterior
   #Estructura = [element for element in iterable if condition] - la condicion es opcional
   lista2 = [i**2 for i in range(1,101) if i%3 != 0]
   print(lista2)
   #lista de los multiplos de 4,6 y 9 hasta 5 digitos
   lista2 = [i for i in range(1,100000) if i%36 == 0]
if __name__ == "__main__":
   listCuadrado()