from typing import ValuesView


def palindrome(string):
   try:
      if len(string) == 0:
         raise ValueError("No puede ingresar una cadena vacia")
      return string == string[::-1]
   except ValueError as ve:
      print(ve) #muestra el mensaje de raise
   return False

try:
   print(palindrome("olo"))
except Exception as e:
   print("Ingrese solo un string")   
   
#finally se ejecuta siempre utilidad para liberar memoria o cierre de archvos
#al igual que cortar la conexion con una bdd
try:
   f = open("../material.txt")
finally:
   f.close()
